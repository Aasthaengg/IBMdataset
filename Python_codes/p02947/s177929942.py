N = int(input())

dic = {}
for _ in range(N):
    s = ''.join(sorted(input()))

    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

ans = 0
for v in dic.values():
    if v >= 2:
        ans += (v*(v-1))//2
print(ans)
