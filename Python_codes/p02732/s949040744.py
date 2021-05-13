n = int(input())
a = list(map(int, input().split()))

c = [0 for i in range(n+1)]
comb = [0 for i in range(n+1)]

for i in range(n):
    c[a[i]] += 1
for i in range(1, n+1):
    if c[i] >= 2:
        comb[i] = int(c[i]*(c[i]-1)/2)

s = sum(comb)
for i in range(n):
    tmp = s - comb[a[i]]
    if c[a[i]]-1 <= 1:
        print(tmp)
    else:
        print(tmp+int((c[a[i]]-1)*(c[a[i]]-2)/2))
