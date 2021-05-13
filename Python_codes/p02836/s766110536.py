s = input()
news = "".join(list(reversed(s[len(s)//2:])))
cnt = 0
for i in range(len(news)):
    if s[i] != news[i]:
        cnt += 1

print(cnt)
