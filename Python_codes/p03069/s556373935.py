N=int(input())
S=input()
acc=S.count(".")
ans=acc
for i in range(N):
    if S[i]=="#":
        acc+=1
    else:
        acc-=1
    ans=min(ans, acc)
print(ans)