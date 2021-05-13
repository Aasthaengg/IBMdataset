N=int(input())
S=input()
leftblack=0
rightwhite=0
for i in range(0,N):
    if S[i]==".":
        rightwhite+=1
ans=leftblack+rightwhite
for i in range(0,N):
    if S[i]=='.':
        rightwhite-=1
    else:
        leftblack+=1
    test=leftblack+rightwhite
    if ans>test:
        ans=test

print(ans)
