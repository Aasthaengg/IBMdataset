n = int(input())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))
clst = list(map(int, input().split()))
alst.sort()
blst.sort()
clst.sort()

b_s = [0 for _ in range(n)]
a_pos = 0
alst.append(10 ** 10)
for i in range(n):
    while blst[i] > alst[a_pos]:
        a_pos += 1
    b_s[i] = a_pos + b_s[i - 1]
b_pos = 0
blst.append(10 ** 10)
ans = 0
for i in range(n):
    while clst[i] > blst[b_pos]:
        b_pos += 1
    if b_pos == 0:
        continue
    ans += b_s[b_pos - 1]
print(ans)