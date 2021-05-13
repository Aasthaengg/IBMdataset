N = int(input())
A = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        x -= 1
        A[i][x] = y 

ans = 0
for b in range(2**N):
    bit = bin(b)[2:].zfill(N)
    flg = True
    for i in range(N):
        if bit[i] == '0': continue
        for j in range(N):
            if A[i][j] == -1: continue
            if A[i][j] != int(bit[j]):
                flg = False
                break
        
        if not flg: break

    ans = max(bit.count('1'), ans) if flg else ans

print(ans)