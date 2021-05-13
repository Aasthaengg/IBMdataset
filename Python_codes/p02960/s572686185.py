K = 1000000007
S = input()
l = len(S)
li = [1] + [0] * 12
work_lists = [[0] * 13 for i in range(6)]
for i in range(6):
    for x in range(10):
        work_lists[i][(x * (10 ** i)) % 13] = 1
for i in range(l):
    s = S[l - i - 1]
    if s == "?":
        work_li = work_lists[i % 6]
        next_li = [sum([work_li[j] * li[(k - j) % 13] for j in range(13)]) % K for k in range(13)]
    else:
        n = int(s)
        r = (n * (10 ** (i % 6))) % 13
        next_li = [li[(j - r) % 13] for j in range(13)]
    li = next_li
print(li[5])
