s = input()
w = int(input())

l = ''

c = 0
while c < len(s):
    l += s[c]
    c += w

print(l)