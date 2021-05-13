from collections import deque

S = input()

q = deque(list(S))
# print(q)
out = []
answer = list("AKIHABARA")
p = 0
while p < 9:
    if q:
        letter = q.popleft()
    else:
        letter = "A"
    # print(p, q)
    if len(q) > 20:
        break
    if letter != answer[p]:
        q.appendleft(letter)
        q.appendleft("A")
    else:
        out.append(letter)
        p += 1

if answer == out and len(q) == 0:
    print("YES")
else:
    print("NO")

