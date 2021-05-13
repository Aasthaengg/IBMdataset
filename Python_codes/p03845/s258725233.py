n = int(input())
T = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    copyT = T.copy()
    p, x = map(int, input().split())
    copyT[p - 1] = x
    print(sum(copyT))