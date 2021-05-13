s=list(input())
k=int(input())
for i in range(len(s)):
    if s[i]!="1":
        p=i+1
        pnum=int(s[i])
        break
    p=101

if k<p:
    print(1)
else:
    print(pnum)