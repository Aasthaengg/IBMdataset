def solve(m,ans):
    global L,S
    if m == len(L):
        S.add(ans)
    else:
        solve(m+1,ans+L[m])
        solve(m+1,ans)

n = int(input())
S = set([])
L = list(map(int,input().split()))
q = int(input())
solve(0,0)
for i in map(int,input().split()):
    if i in S:
        print("yes")
    else:
        print("no")
