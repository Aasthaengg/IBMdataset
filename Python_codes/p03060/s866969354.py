N=int(input())
value=list(map(int,input().split()))
cost=list(map(int,input().split()))

a=0
for v,c in zip(value,cost):
    if v>c:
        a+=v-c
        
print(a)