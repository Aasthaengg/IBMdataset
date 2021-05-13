from collections import Counter, defaultdict, deque
s = input()
#n,a,b = map(int,input().split())
# al = list(map(int,input().split()))

b = 0
ans = 0
for i in range(len(s)):
    if s[i] == 'B':
        b += 1
    elif s[i] == 'W':
        ans += b
    else:
        b = 0
print(ans)