n = int(input())
S = [''.join(sorted(input())) for _ in range(n)]
cnt = 0
dic = {}
for s in S:
    if s in dic.keys():
        cnt += dic[s]
        dic[s] += 1
    else:
        dic[s] = 1
print(cnt)