import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n,k = map(int,readline().split())
lst1 = list(map(int,readline().split()))

"""
lst1に関しての全ての1の出現回数を求め、
lst1の半分より(1の出現回数が多いなら)多いならkのその桁を0に、
少ないならkのその桁を1にすることによってfは最大化される。

ただし、kには制約があるので、上位桁を優先として、制約内に収まる答えを探す。
"""
k = bin(k)
k = k[2:]
lst2 = [0]*40

for i in lst1:
    for j in range(40):
        if i >> j & 1:
            lst2[j] += 1 #1が入っているなら1足す。
lst2.reverse()
lst2 = lst2[40-len(k):]
th = n//2 #1の数がこれを下回る(th>X)場合、その桁を1にしたほうが良い

free = 0 #自由に下位桁を決められるようになったら1にする
res = 0
for i in range(len(k)):
    if not free:
        if k[i] == "1":
            if lst2[i] <= th:
                res += 1 << len(k)-1-i
            else:
                free = 1
    else:
        if lst2[i] < th:
                res += 1 << len(k)-1-i


ans = 0
for i in lst1:
    ans += i^res
print(ans)