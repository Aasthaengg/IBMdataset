n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(n):
    a[i] %= 2

count_1=a.count(1)
if count_1 % 2 == 0:
    print("YES")
else:
    print("NO")