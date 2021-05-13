n = int(input())
a = list(map(int,input().split()))
ans1,ans2 = 0,0
sum1,sum2 = 0,0
for i in range(n):
    sum1 += a[i]
    if i%2 == 1 and sum1 >= 0:
        ans1 += sum1 + 1
        sum1 = -1
    elif i%2 == 0 and sum1 <= 0:
        ans1 += -sum1 + 1
        sum1 = 1
for i in range(n):
    sum2 += a[i]
    if i%2 == 0 and sum2 >= 0:
        ans2 += sum2 + 1
        sum2 = -1
    elif i%2 == 1 and sum2 <= 0:
        ans2 += -sum2 + 1
        sum2 = 1
print(min(ans1,ans2))
