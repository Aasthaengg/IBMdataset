from sys import stdin


def solve():
    r,c = [int(i) for i in stdin.readline().split()]
    A = []
    for _ in range(r):
        k = str(input())
        l = [1 if i == '.' else '#' for i in k]
        A.append(l)
    pre = False
    for i in range(c):
        if pre: A[0][i] = '#'
        elif A[0][i] == '#': pre = True
    for i in range(1, r):
        for j in range(c):
            if A[i][j] == '#': continue
            elif j == 0: A[i][j] = A[i-1][j]
            elif A[i-1][j] == '#' and A[i][j-1] == '#': A[i][j] = '#'
            elif A[i-1][j] == '#': A[i][j] = A[i][j-1]
            elif A[i][j-1] == '#': A[i][j] = A[i-1][j]
            else: A[i][j] = A[i][j-1] + A[i-1][j]
    if A[-1][-1] == '#': return 0
    else: return A[-1][-1] % ((10**9) + 7)

print(solve())