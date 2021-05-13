import copy

def warshall_floyd(d,n):
    D = copy.deepcopy(d) 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == k  or k == j:
                    continue
                if d[i][k] + d[k][j] < d[i][j]:
                    return -1 
                elif d[i][k] + d[k][j] == d[i][j]:
                    D[i][j] = 0
    ans = sum([sum(i) for i in D])
    assert not (ans % 2)
    return ans // 2
  
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
ans = warshall_floyd(a,n)
print(ans)