N=int(input())
a=list(map(int,input().split()))
t=0
for i in a:
    t=t^i
print("No" if t else "Yes")