n = int(input())
A = list(map(int,input().split()))
ball = [0]*(n) #入ってたら１

#ｎからn//2+1まで、Ａが１ならballも１
for i in reversed(range(n//2+1, n+1)):
    if A[i-1] == 1:
        ball[i-1] = 1

#n//2から１まで、その倍数をピックアップし、Ｂａｌｌを見る
for i in reversed(range(1, n//2+1)):
    s = n//i
    now = 0
    for j in range(2,s+1):
        if ball[i*j-1] == 1:
            now += 1
    if A[i-1] != now%2:
        ball[i-1] = 1

ans = []
for i in range(n):
    if ball[i] == 1:
        ans.append(i+1)
print(len(ans))
print(*ans)