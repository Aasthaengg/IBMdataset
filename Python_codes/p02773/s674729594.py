from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(N):
    s = input()
    dic[s]+=1
m = 0
for i in dic:
    m = max(m, dic[i])
ans = []
for i in dic:
    if dic[i]==m:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)