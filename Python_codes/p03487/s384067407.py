N = int(input())
*A, = map(int, input().split())
dic = {}
ans = 0
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
for k, v in dic.items():
    if k == v:
        continue
    elif k > v:
        ans += v
    else:
        ans += v - k
print(ans)
