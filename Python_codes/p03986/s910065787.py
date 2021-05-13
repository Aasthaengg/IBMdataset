from queue import Queue

S = input()
ans = len(S)
Q = Queue()
for s in S:
    if s == 'S':
        Q.put(s)
    else:
        if Q.empty():
            continue
        Q.get()
        ans -= 2
print(ans)
