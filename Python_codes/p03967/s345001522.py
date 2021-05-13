s = input()
length_s = len(s)
paper_cnt = 0
ans = 0

for i in range(length_s):
    if s[i] == 'g':
        if paper_cnt < 0:
            ans += 1
            paper_cnt += 1

        else:
            paper_cnt -= 1

    else:
        if paper_cnt < 0:
            paper_cnt += 1

        else:
            ans -= 1
            paper_cnt -= 1

print(ans)
