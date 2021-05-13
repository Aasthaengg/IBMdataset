n = int(input())
li_v = list(map(int, input().split()))
li_c = list(map(int, input().split()))
s = 0
for i in range(n):
  if li_v[i] - li_c[i]>=0:
    s += li_v[i] - li_c[i]
print(s)