from collections import deque
import heapq

s = input()
s += " "

S = ""

for i in range(len(s)-1):
    if s[i] == "B" and s[i+1] == "C":
        S += "Z"

    elif i > 0 and s[i] == "C" and s[i-1] == "B":
        continue
    else:
        S += s[i]

#print (S)
la = deque([])
ans = 0
for i in range(len(S)):

    if S[i] == "A":
        la.append(i)

    elif S[i] == "Z" and len(la) > 0:
        lastA = la.popleft()
        ans += i - lastA
        la.append(i)

    else:
        la = deque([])

print (ans)
