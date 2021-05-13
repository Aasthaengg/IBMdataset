n=int(input())
a=0
b=0
for i in range(n):
    A,B=map(int,input().split())
    a=max(a,A)
    if a==A:
        b=B
print(a+b)