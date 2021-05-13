eList = [chr(i) for i in range(97, 97+26)]
N = int(input())

n = N
mod = N
numList = []

while n > 0:
    n, mod = divmod(n, 26)
    if mod != 0:
        # 末尾ではなく先頭に追加する
        # 1のくらいから判定して行っているため
        numList.insert(0, mod - 1)
    else:
        numList.insert(0, 25)
        # 26進数のようで26まで数字があるため調整する
        n -= 1

ans = ''
for num in numList:
    ans += eList[num]
print(ans)