N=int(input())
S=input()

numb=[0]
numw=[0]
cond="b"
for i in range(N):
    numb.append(numb[-1])
    numw.append(numw[-1])
    if S[i]=="#":
        numb[-1]+=1
    else:
        numw[-1]+=1

ans=[0 for _ in range(N+1)]
for j in range(N+1):
    ans[j]=numb[j]+(numw[-1]-numw[j])
print(min(ans))