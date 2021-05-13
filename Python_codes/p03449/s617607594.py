n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

ml = [[0 for i in range(n)] for j in range(2)]

for i in range(n):
    if i==0:
        ml[0][i] = l1[i]
    else:
        ml[0][i] = ml[0][i-1] + l1[i]
for i in range(n):
    if i==0:
        ml[1][i] = ml[0][i] + l2[i]
    else:
        ml[1][i] = max(ml[0][i], ml[1][i-1]) + l2[i]

print(ml[1][n-1] , flush=True)
