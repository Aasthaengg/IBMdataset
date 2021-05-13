n,m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

ans = 'No'
for di,dj in [(pi,pj) for pi in range(n-m+1) for pj in range(n-m+1)]:
    for i,j in [(pi,pj) for pi in range(m) for pj in range(m)]:
        if a[di+i][dj+j] != b[i][j]:
            break
    else:
        ans = 'Yes'
        break
print(ans)
