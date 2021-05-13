import collections

N = int(input())
table = [int(input()) for _ in range(N)]

ans = 0
cnt = collections.Counter(table).most_common()

for i in cnt:
    if i[1] % 2 != 0:
        ans += 1

print(ans)
exit()
