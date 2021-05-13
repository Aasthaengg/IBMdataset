import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def Zalgo(S):
    N = len(S)
    A = [0]*N

    froms = -1
    lasts = -1
    for i in range(1, N):
        same = 0
        if froms != -1:
            same = min(A[i-froms], lasts-i)
            same = max(0, same)
        while i+same<N and S[same] == S[i+same]:
            same += 1
        
        if i+same > lasts:
            lasts = i+same
            froms = i
        A[i] = same
    A[0] = N
    return A

N = int(input())
S = input().rstrip()

ans = 0
for i in range(N):
    A = Zalgo(S[i:])
    res = 0
    L = len(A)
    for j,a in enumerate(A):
        res = max(res, min(j, a))
    ans = max(res, ans)
print(ans)