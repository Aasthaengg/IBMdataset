n = int(input())
A = tuple(map(int, input().split()))
q = int(input())
M = tuple(map(int, input().split()))

sums = set()
from collections import deque
st = deque([[0, 0], [0, A[0]]])
while st:
    i, s = st.pop()
    i += 1
    if i == n:
        sums.add(s)
        continue
    st.append([i, s])
    st.append([i, s+A[i]])

for m in M:
    print('yes' if m in sums else 'no')
    
