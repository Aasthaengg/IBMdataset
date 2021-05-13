n, q = list(map(int, input().split()))
s = input()

cnt = [0 for i in range(n)]
ac = 0
for i in range(1, n):
    if s[i-1:i+1] == "AC":
        ac += 1

    cnt[i] = ac

for i in range(q):
    l, r = list(map(int, input().split()))

    print(cnt[r-1]-cnt[l-1])