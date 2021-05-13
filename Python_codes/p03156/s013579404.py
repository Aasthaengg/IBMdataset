n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
one=0
two=0
three=0
for i in range(n):
    if p[i]<=a:
        one+=1
    elif b+1>p[i]>a:
        two+=1
    else:
        three+=1
print(min(one,two,three))
