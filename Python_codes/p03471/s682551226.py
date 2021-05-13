N, Y = map(int, input().split())

ans = [-1, -1, -1]
findit = False
sen = 0
for man in range(N + 1):
    for gosen in range(N + 1):
        sen = N - man - gosen
        if (man * 10000) + (gosen * 5000) + (sen * 1000) == Y and 0 <= sen:
            ans = [man, gosen, sen]

str_ans = map(str, ans)
print(" ".join(str_ans))