S = list(input())
a = 0
for i in S:
    if i == 'R':
        a += 1
if a == 2:
    if S[1] == 'S':
        a = 1
print(a)
