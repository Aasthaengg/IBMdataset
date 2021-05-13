import sys
n, k = map(int, input().split())
s = input()

if n == 1:
    print(0)
    sys.exit()

# L...L|R...R|L...L|...と分解
# 奇数番目をflip
s1 = []
flip_count = 0
for i in range(n):
    if flip_count < k and s[i] == s[0]:
        s1.append('R' if s[0]=='L' else 'L')
    else:
        s1.append(s[i])
    if i < n-1 and s[i] == s[0] and s[i+1] != s[0]:
        flip_count += 1

# 偶数番目をflip
s2 = []
flip_count = 0
for i in range(n):
    if flip_count < k and s[i] != s[0]:
        s2.append('L' if s[0]=='L' else 'R')
    else:
        s2.append(s[i])
    if i < n-1 and s[i] != s[0] and s[i+1] == s[0]:
        flip_count += 1

ans1, ans2 = 0, 0
i = 0
while True:
    if i == 0:
        if s1[i] == 'R' and s1[i+1] == 'R': ans1 += 1
    elif i == n-1:
        if s1[i] == 'L' and s1[i-1] == 'L':
            ans1 += 1
            break
    else:
        if s1[i] == 'R' and s1[i+1] == 'L':
            i += 1
        else:
            ans1 += 1
    i += 1
    if i > n-1:
        break

i = 0
while True:
    if i == 0:
        if s2[i] == 'R' and s2[i+1] == 'R': ans2 += 1
    elif i == n-1:
        if s2[i] == 'L' and s2[i-1] == 'L':
            ans2 += 1
            break
    else:
        if s2[i] == 'R' and s2[i+1] == 'L':
            i += 1
        else:
            ans2 += 1
    i += 1
    if i > n-1:
        break

print(max(ans1, ans2))
