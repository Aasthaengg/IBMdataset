n, a, b, c, d = map(int, input().split())
s = input()

res = 'Yes'

for i in range(a-1, c-1):
    if s[i] == s[i+1] == '#':
        res = 'No'
        break

if res != 'No':
    if c < d:
        for i in range(b-1, d-1):
            if s[i] == s[i+1] == '#':
                res = 'No'
                break
    else:
        for i in range(b-2, d-1):
            if s[i] == s[i+1] == s[i+2] == '.':
                break
        else:
            res = 'No'

print(res)
