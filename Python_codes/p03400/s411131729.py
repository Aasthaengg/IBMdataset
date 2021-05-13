n=int(input())
d,x = map(int,input().split())
a=[int(input()) for i in range(n)]
a1 = 0

for i in range(len(a)):
    a1 = int((d-1)/a[i])+1
    x += a1


print(x)