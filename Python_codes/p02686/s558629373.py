n = int(input())
plus = []
minus = []
for i in range(n):
    s = input()
    mini = 0
    ruikei = 0
    for j in range(len(s)):
        if s[j] == '(':
            ruikei += 1
        else:
            ruikei -= 1
            mini = min(mini, ruikei)
    if ruikei > 0:
        plus.append([mini, ruikei])
    else:
        mini = 0
        ruikei = 0
        for j in range(len(s))[::-1]:
            if s[j] == ')':
                ruikei += 1
            else:
                ruikei -= 1
                mini = min(mini, ruikei)
        minus.append([mini, ruikei])

plus.sort(reverse=True, key=lambda x: x[0])
minus.sort(reverse=True, key=lambda x: x[0])

ans = 'Yes'
top_plus = 0
for i in range(len(plus)):
    mini, ruikei = plus[i]
    if top_plus + mini < 0:
        ans = 'No'
        break
    else:
        top_plus += ruikei

top_minus = 0
for i in range(len(minus)):
    mini, ruikei = minus[i]
    if top_minus + mini < 0:
        ans = 'No'
        break
    else:
        top_minus += ruikei

if top_plus != top_minus:
    ans = 'No'

print(ans)