n=int(input())
max=0
max_point=0
for i in range(n):
    a,b=map(int,input().split())
    if max<a:
        max=a
        max_point=b
print(max+max_point)
