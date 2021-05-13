N = int(input())
bbb = list(map(int, input().split()))
aaa = []
for i in range(1, N - 1):
    a = min(bbb[i - 1], bbb[i])
    aaa.append(a)
print(sum(aaa) + bbb[0] + bbb[-1])
