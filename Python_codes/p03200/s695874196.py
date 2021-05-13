s=list(input())

num = s.count('W')

before = 0
for i in range(len(s)):

    if s[i]=='W':
        before += i


after = 0
for j in range(num):
    after+=j

print(before-after)