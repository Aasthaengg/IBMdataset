#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())
v=0
for st in s:
    if st=="+":
        v+=1
    else:
        v-=1
print(v)
