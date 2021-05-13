N = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
total = sum(aaa)
for i in range(N - 1, -1, -1):
    if aaa[i + 1] > bbb[i]:
        aaa[i + 1] -= bbb[i]
    else:
        bbb[i] -= aaa[i + 1]
        aaa[i + 1] = 0
        aaa[i] = max(0, aaa[i] - bbb[i])
print(total - sum(aaa))
