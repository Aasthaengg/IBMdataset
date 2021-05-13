a,b=map(int,input().split())
score=0
n=0
while n<2:
    if a>b:
        score+=a
        a-=1
    else:
        score+=b
        b-=1
    n+=1
print(score)