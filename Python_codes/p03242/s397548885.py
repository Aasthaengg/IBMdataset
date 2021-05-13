inf = 10**15
mod = 10**9+7

n = input()
ans = ''
for c in n:
    if c == '1':
        ans = ''.join([ans, '9'])
    else:
        ans = ''.join([ans, '1'])
print(ans)