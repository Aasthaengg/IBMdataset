n=int(input())
s=input()

cnt=0
maxcnt=0

for i in range(n):
    if s[i]=="I":
        cnt+=1
    else:
        cnt-=1
    maxcnt=max(maxcnt,cnt)
print(maxcnt)