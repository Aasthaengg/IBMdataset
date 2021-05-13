n, k = map(int, input().split())
s = list(map(int, list(input())))

i = 0
a = []
while i < n:
    l = 1
    while i+1 < n and s[i]==s[i+1]:
        l+=1
        i+=1
    a.append(l)
    i+=1

if s[0] == 0:
    a = [0] + a
if s[-1] == 0:
    a = a + [0]
n = len(a)

acum = [0]*(n+1)
for i in range(n):
    acum[i+1] = acum[i]+a[i]

ans = 0
for i in range(0, n, 2):
    end = min(i+2*k+1, n)
    ans = max(ans, acum[end] - acum[i])
print(ans)