from collections import deque 
S = deque(input())
T = input()

result = 'No'
for i in range(len(S)):
    a = S.pop()
    S.appendleft(a)
    if ''.join(S) == T:
        result = 'Yes'
        break
print(result)