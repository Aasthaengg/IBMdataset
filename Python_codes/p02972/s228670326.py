N = int(input())
a = list(map(int, input().split()))
ans = [0]*N
anss = []
ball = 0
for i in range(N, 0, -1):
    count = N//i
    total = 0
    for j in range(1, count+1):
        total += ans[i*j-1]
    if total%2 == a[i-1]:
        ans[i-1] = 0
    else:
        ans[i-1] = 1
        anss.append(i)
        ball += 1
if ball == 0:
    print(0)
else:
    print(ball)
    anss.reverse()
    print(" ".join(map(str, anss)))
