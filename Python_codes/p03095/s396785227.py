mod = 10**9+7
n = int(input())
s = input()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
result = 1
for i, j in d.items():
    result = (result*(j+1))%mod

print((result-1)%mod)