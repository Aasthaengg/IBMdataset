N = int(input())
A = list(map(int, input().split()))
ls = [(A[i], i) for i in range(N)]
ls.sort()
ans = [ls[i][1]+1 for i in range(N)]
print(*ans)