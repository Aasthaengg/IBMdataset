N, Y = map(int, input().split())
Y = Y//1000

def solve(N, Y):
    for i in range(N+1):
        for j in range(N+1-i):
            res = 10*i + 5*j + (N-i-j)
            if res == Y:
                return i, j, N-i-j
    else:
        return -1, -1, -1

ans = solve(N, Y) 
print(*ans)