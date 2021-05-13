n, a, b, c, d = map(int, input().split())
s = input()

a = a-1
b = b-1
c = c-1
d = d-1

for i in range(a+1, d):
    if s[i-1] == '#' and s[i] == '#':
        print('No')
        exit()

if c < d:
    print('Yes')
    exit()

for i in range(b, d+1):
    if s[i-1] == '.' and s[i] == '.' and s[i+1] == '.':
        print('Yes')
        exit()
print('No')
