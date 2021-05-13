N = int(input())
s = {}
for i in range(N):
    str = input()
    if str in s:
        s[str]+=1
    else:
        s[str] = 1
M = int(input())
for j in range(M):
    str = input()
    if str in s:
        s[str]-= 1
    else:
        s[str] = -1
if max(s.values()) < 0:
    print(0)
else:
    print(max(s.values()))