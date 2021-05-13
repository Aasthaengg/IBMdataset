n, a, b=map(int, input().split())
sum1=0
for i in range(n):
    num=str(i+1)
    sum2=0
    for j in range(len(num)):
        sum2+=int(num[j])
    if sum2>=a and sum2<=b:
        sum1+=i+1
print(sum1)
