n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]
cnt = [0]*10**5
ans = sum(a)
for i in a:
    cnt[i-1] += 1

for i in range(q):
    b, c = bc[i][0], bc[i][1]
    ans += (c - b)*cnt[b-1]
    cnt[c-1] += cnt[b-1]
    cnt[b-1] = 0
    print(ans)
