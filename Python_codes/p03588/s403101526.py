n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
ab.sort()
print(ab[-1][0] + ab[-1][1])