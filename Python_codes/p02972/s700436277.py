n = int(input())
a = list(map(int, input().split()))
ball = [0] * n

for i in range(n)[::-1]:
    m = n//(i+1)
    count = 0
    for j in range(1, m+1):
        count += ball[j*(i+1)-1]
    ball[i] = (a[i]%2)^(count%2)

print(sum(ball))
for i in range(n):
    if ball[i] == 1:
        print(i+1)