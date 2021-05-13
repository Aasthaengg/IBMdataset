n = int(input())
a = list(map(int, input().split()))

ball = [0]*n

for i in reversed(range(1, n+1)):

    ball_in_or_not = a[i-1] ^ sum(ball[i-1:n:i]) % 2
    
    if ball_in_or_not == 1:
        ball[i-1] =1

if sum(ball) > 0:
    print(sum(ball))
    print(*[i+1 for i in range(n) if ball[i] > 0]) 

else:
    print(0)