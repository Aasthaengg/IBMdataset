H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

ans = []
num = 1
count = 0
for i in range(H):
    tmp = []
    if i % 2 == 0:
        for j in range(W):
            tmp.append(str(num))
            count += 1
            if count == a[num - 1]:
                num += 1
                count = 0
        ans.append(tmp)
    else:
        for j in range(W):
            tmp.insert(0, str(num))
            count += 1
            if count == a[num - 1]:
                num += 1
                count = 0
        ans.append(tmp)


for i in range(len(ans)):
    print(" ".join(ans[i]))
