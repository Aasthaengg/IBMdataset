N = int(input())
dic = {}
for _ in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
ma = max(dic.values())
for i,j in sorted(dic.items()):
    if j == ma:
        print(i)