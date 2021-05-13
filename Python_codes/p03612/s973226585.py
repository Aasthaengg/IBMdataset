N=int(input())
P=list(map(int,input().split()))
S=["x" if P[i]==i+1 else "o" for i in range(N)]
count=0
for j in range(N-1):
    if S[j]=="x":
        S[j]="o"
        if S[j+1]=="x":
            S[j+1]="o"
        count+=1
if S[N-1]=="x":
    count+=1
print(count)