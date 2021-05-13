N = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
ccc = list(map(int, input().split()))
acc = 0
for j in range(N - 1):
    i = aaa[j] - 1
    acc += bbb[i]
    if aaa[j] + 1 == aaa[j + 1]:
        acc += ccc[i]
else:
    acc += bbb[aaa[-1] - 1]
print(acc)
