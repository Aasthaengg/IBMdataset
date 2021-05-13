import sys
input = sys.stdin.readline

s = input()[:-1]
A = 0
ans = 0
i = 0

while i<len(s):
    if s[i]=='A':
        A += 1
        i += 1
    else:
        if i+1<len(s) and s[i:i+2]=='BC':
            ans += A
            i += 2
        else:
            A = 0
            i += 1

print(ans)