A,B=map(int,input().split())
count=0
for C in range(A,B+1):
    s=str(C)
    res=True
    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            res=False
            break

    if res:
        count+=1

print(count)
