from itertools import combinations_with_replacement as cwr
n,m,q=map(int,input().split())
abcd = [list(map(int,input().split())) for _ in range(q)]

def calscore(A):
    score = 0
    for a,b,c,d in abcd:
        if A[b-1] -A[a-1] ==c:
            score += d
    return score

ans =0
for A in cwr(range(1,m+1),n):
    ans = max(ans, calscore(A))
print(ans)