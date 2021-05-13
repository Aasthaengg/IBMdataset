A, B, M = map(int, input().split())  #数字
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pr = []
for i in range(M):
    X = list(map(int, input().split()))  #リスト

    pr.append(a[X[0]-1] + b[X[1]-1] - X[2])

print(min(min(a)+min(b),min(pr)))