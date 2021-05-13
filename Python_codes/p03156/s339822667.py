n=int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
s1=s2=s3=0
for i in range(n):
    if p[i]<=a:
        s1+=1
    elif p[i]<=b:
        s2+=1
    else:
        s3+=1
print(min(s1,s2,s3))



