n = int(input())

b = list(map(int,input().split()))

Flag = True

memo = []

while Flag:
    Flag = False
    index = -1
    for i, v in enumerate(b):
        if i == v-1:
            Flag = True
            index = i
    if index != -1:
        m = b.pop(index)
        memo.append(m)
if len(b):
    print(-1)
else:
    memo.reverse()
    for aa in memo:
        print(aa)