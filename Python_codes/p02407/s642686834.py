n =int(input())
a = list(map(int,input().split()))
a.reverse()
for i in range(n):
    if i!=n-1:
        print(a[i],end=" ")
    else:
        print(a[i])