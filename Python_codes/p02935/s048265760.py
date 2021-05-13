n = int(input())
a = list(map(int,input().split()))
a.sort()
sum = a[0]
for i in range(1,n):
    sum = (sum + a[i])/2
print(sum)