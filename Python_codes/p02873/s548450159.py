S = input().strip()
N = len(S)+1
A = [0 for _ in range(N)]
flag = -1
B = []
for i in range(N-1):
    if flag==-1 and S[i]=="<":
        B.append(i)
        flag = 1
    elif flag==1 and S[i]==">":
        flag = -1
if flag==-1:
    B.append(N-1)
for b in B:
    for i in range(b,N-1):
        if S[i]=="<":
            A[i+1] = max(A[i+1],A[i]+1)
        else:break
    for i in range(b-1,-1,-1):
        if S[i]==">":
            A[i] = max(A[i],A[i+1]+1)
        else:break
print(sum(A))