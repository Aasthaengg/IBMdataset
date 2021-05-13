N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
print(sorted(A)[-1][0] + sorted(A)[-1][1])