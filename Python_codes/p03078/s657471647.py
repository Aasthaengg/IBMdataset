X,Y,Z,K = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=1)
B = sorted(list(map(int,input().split())),reverse=1)
C = sorted(list(map(int,input().split())),reverse=1)
num= []
for xi in range(1,X+1):
    for yi in range(1,Y+1):
        for zi in range(1,K//(xi*yi)+1):
            if xi*yi*zi <= K and zi < Z+1:
                num.append((xi-1,yi-1,zi-1))

ans = []
for a,b,c in num:
    ans.append(A[a]+B[b]+C[c])
ans.sort(reverse=1)
for i in range(K):
    print(ans[i])