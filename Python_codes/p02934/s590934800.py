n=int(input())
l = list(map(int,input().split()))
a=1
for i in l:
    a=a*i
b=0
for i in l:
    b+=a/i
print(a/b)