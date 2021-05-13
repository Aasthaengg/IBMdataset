s = str(input())
t = str(input())
ans = []
for i in range(len(s) - len(t) + 1):
    if s[i] == t[0] or s[i] == '?':
        for j in range(len(t)):
            if not(s[i+j] == t[j] or s[i+j] == '?'):
                break
        else:
            news = s[:i] + t + s[i+len(t):]
            news = news.replace('?', 'a')
            ans.append(news)
ans.sort()
if ans:
    print(ans[0])
else:
    print('UNRESTORABLE')
