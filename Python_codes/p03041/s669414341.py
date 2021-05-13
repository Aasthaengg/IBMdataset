n, k = map(int, input().split())

s = input()

if s[k-1] == 'A':
    t = 'a'
elif s[k-1] == 'B':
    t = 'b'
elif s[k-1] == 'C':
    t = 'c'

s = s[:k-1] + t + s[k:]

print(s)