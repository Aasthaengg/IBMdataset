A="abcdefghijklmnopqrstuvwxyz"
S=input()
k=int(input())
n=len(S)

C=[]

for a in A:
    now=""
    cnt=0
    if not a in S:
        continue
    for i in range(n):
        if S[i]==a:
            for j in range(5):
                if i+j<n:
                    C.append(S[i:i+j+1])
                else:
                    break
    C.sort()
    for c in C:
        if now!=c:
            now=c
            cnt+=1
        if cnt==k:
            break
    if cnt==k:
        break
print(now)        