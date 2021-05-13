from collections import Counter
def solve():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    D = [[0,0],[0,0]]
    for k,v in C.items():
        if v>=2:
            D.append([k,v])
    D.sort(reverse=True)
    if D[0][1]>=4:
        return D[0][0]**2
    return D[0][0]*D[1][0]
print(solve())