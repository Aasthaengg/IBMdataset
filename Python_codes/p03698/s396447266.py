S = input()
s = [S[0]]
ans = 'yes'

for i in S[1:]:
    if i in s:
        ans = 'no'
        break
    else:
        s.append(i)
print(ans)