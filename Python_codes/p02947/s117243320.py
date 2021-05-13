n = int(input())
s = [" ".join(sorted(input())) for _ in range(n)]

count = 0
dic = {}

for a in s:
    if a in dic.keys():
        count += dic[a]
        dic[a] += 1
    else:
        dic[a] = 1

print(count)