def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())
def lim(N):
    return [int(input()) for i in range(N)]

N = ii()
A = li()

bunbo = 0

for i in range(N):
    bunbo += 1 / A[i]

print(1 / bunbo)