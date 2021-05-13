n=int(input())
f=0
for i in range(n):
    s=int(input())
    if s%2==0:
        f+=1
print("second" if f==n else "first" )