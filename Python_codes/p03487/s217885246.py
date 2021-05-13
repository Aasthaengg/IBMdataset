N = int(input())
a = list(map(int, input().split()))
dic = {}
ans = 0
for i in range(N):
    if not a[i] in dic:
        dic[a[i]] = 0
    dic[a[i]] += 1

for k, v in dic.items():
    if k < v:
        ans += v-k
    if k > v:
        ans += v

print(ans)