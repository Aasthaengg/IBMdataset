n = int(input())
t,a = map(int, input().split())
h = list(map(int, input().split()))

ans = 1000000
cnt = 0
T = [0 for i in range(n)]

for i in range(n) :
    T[i] = t - h[i]*0.006
    q = abs(a - T[i]) 
    if (q < ans) :
        ans = q
        cnt = i+1
print(cnt)