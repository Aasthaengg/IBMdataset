s = input()
n = len(s) - 1
answers = []
sl = [s[i] for i in range(len(s))]
for i in range(2 ** n):
    tmp = []
    for j in range(n):
        if ((i >> j) & 1):
            tmp.append(j)
    ll = ['*']*len(s)
    for k in tmp:
        ll[k] = '+'
    ans = []
    for k, _ in zip(sl, ll):
        ans.append(k)
        ans.append(_)
    ans = [_ for _ in ans if _ != '*']
    ans = ''.join(ans)
    ans = ans.split('+')
    ans = [int(_) for _ in ans if _ != '+']
    ans = sum(ans)
    answers.append(ans)
print(sum(answers))
