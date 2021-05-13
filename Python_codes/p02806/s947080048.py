n=int(input())
a=[list(input().split()) for i in range(n)]
x=input()
b=0
for i in range(n):
    b+=int(a[i][1])
for i in range(n):
    b-=int(a[i][1])
    if a[i][0]==x:
        print(b)