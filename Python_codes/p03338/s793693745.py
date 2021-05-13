n=int(input())
s=input()
alphabet=[chr(i) for i in range(97,97+26)]
ans=0

for i in range(1,n):
    s1=s[:i]
    s2=s[i:]
    cnt=0
    for j in range(len(alphabet)):
        if s1.count(alphabet[j])>=1 and s2.count(alphabet[j])>=1:
            cnt+=1
    if cnt>ans:
        ans=cnt
print(ans)