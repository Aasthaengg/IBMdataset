N = int(input())
card = list(map(int, input().split()))
dic = {}
for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
ans = 0
for value in dic.values():
    if value > 1:
        ans += value - 1
print(N-(ans+(ans % 2)))