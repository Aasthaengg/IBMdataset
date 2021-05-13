S = input().rstrip()
N = len(S)
K = int(input())
A = []
for i in range(N):
    A.append(S[i:])
A.sort()
B = set()
flg = False
for i in range(len(A)):
    for j in range(1,len(A[i])+1):
        B.add(A[i][:j])
        if len(B)==K:
            flg = True
            break
    if flg: break
B = list(B)
B.sort()
print(B[-1])