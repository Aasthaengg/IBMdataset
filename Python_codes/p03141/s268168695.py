n=int(input())

score=[]
bsum=0

for _ in range(n):
    a,b=map(int,input().split())
    score.append(a+b)
    bsum-=b

score.sort(reverse=True)

for i,v in enumerate(score):
    if i%2==0:
        bsum+=v

print(bsum)