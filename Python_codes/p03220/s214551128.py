n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

tmp = 10**7
for i in range(n):
    c = abs(a-(t-h[i]*0.006))
    if c < tmp:
        tmp = c
        ans = i+1
print(ans)