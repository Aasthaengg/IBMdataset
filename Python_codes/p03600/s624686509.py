N = int(input())
INF = 10**12
A = []

for i in range(N):
    tmp = list(map(int,input().split()))
    A.append(tmp)

def check():
    c = [[0]*N for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            flag = True
            for k in range(N):    
                if k == i or k == j:
                    continue
                if A[i][j] == A[i][k] + A[k][j]:
                    flag = False
                    break
                elif A[i][j] > A[i][k] + A[k][j]:
                    return -1
            if flag:
                c[i][j] = A[i][j]
    for i in range(N):
        ans += sum(c[i])
    return ans // 2

print(check())
