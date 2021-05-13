import sys

N = int(input())
S = input()
num = len(S)
ans, count = 0, 0
for i in range(1, num):
    a = set(S[:i])
    b = set(S[i:])
    for j in a:
        if j in b: count += 1
    ans = max(ans, count)
    count = 0
    
print(ans)
