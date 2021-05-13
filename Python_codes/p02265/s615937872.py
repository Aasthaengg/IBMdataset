from collections import deque
n = int(input())
deq = deque([])
for i in range(n):
    A = input().split()
    a = A[0]
    if len(A) == 2:
        b = A[1]
    if a == "insert":
        deq.appendleft(b)
    elif a == "deleteFirst":
        deq.popleft()
    elif a == "deleteLast":
        deq.pop()
    else:
        try:
            deq.remove(b)
        except:
            continue
print(" ".join(list(deq)))
