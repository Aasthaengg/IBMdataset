"""
index = j を満たすもののうち最大のものを消していく
→消した番号の逆順が答え
"""
n = int(input())
b = list(map(int, input().split()))

ans = []

while len(b) != 0:
    index = -1
    for j in range(len(b)):
        if j+1 == b[j]:
            index = j

    if index == -1:
        print(-1)
        exit()
    else:
        ans.append(b.pop(index))

for _ans in ans[::-1]:
    print(_ans)
