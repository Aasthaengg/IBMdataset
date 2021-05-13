n=int(input())
s=input()
res=0
for i in range(1,n):
    a=s[:i]
    b=s[i:]
    sum=0
    for j in range(97,123):
        x=chr(j)
        if x in a and x in b:
            sum+=1
    res=max(sum,res)
print(res)
