N = int(input())
cnt_li = [0, 0, 0, 0, 0]
comb = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 1, 4],
    [0, 2, 3],
    [0, 2, 4],
    [0, 3, 4],
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 4],
    [2, 3, 4],
]
for _ in range(N):
    s = input()
    if s[0] == 'M':
        cnt_li[0] += 1
    if s[0] == 'A':
        cnt_li[1] += 1
    if s[0] == 'R':
        cnt_li[2] += 1
    if s[0] == 'C':
        cnt_li[3] += 1
    if s[0] == 'H':
        cnt_li[4] += 1
ans = 0
for i in range(len(comb)):
    one, two, three = comb[i]
    mid = cnt_li[one] * cnt_li[two] * cnt_li[three]
    ans += mid
print(ans)
