N = int(input())
A = list(map(int, input().split()))
dic = {}

for num in A:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

total = 0
for value in dic.values():
    total += value * (value-1) / 2   # 使えないボールがない場合のtotal

for num in A:
    print(int(total - dic[num] + 1))
