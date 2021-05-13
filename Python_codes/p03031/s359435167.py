n,m = map(int,input().split())
k = []
s = []

for i in range(m):
  k.append(list(map(int,input().split())))
  s.append(k[i].pop(0))
p = list(map(int,input().split()))

light_on = 0
switch_on = 0
ans = 0
for i in range(2**n):
  light_on = 0
  for j in range(m):
    switch_on = 0
    for K in range(s[j]):
      if (i >> k[j][K]-1) &1:
        switch_on += 1
    if switch_on%2 == p[j]:
      light_on += 1
  if light_on == m:
    ans  += 1
print(ans)