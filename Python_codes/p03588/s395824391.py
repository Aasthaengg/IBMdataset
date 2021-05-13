from operator import itemgetter
n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

ab.sort(key=itemgetter(0))
ans = ab[0][0]-1 + ab[-1][1] + (ab[-1][0] - ab[0][0] + 1)
print(ans)