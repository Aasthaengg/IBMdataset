from collections import deque

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
steps = list()

A_pos = [x for x in A if x >= 0]  # プラスとして使うもの
A_minus = [x for x in A if x < 0]  # マイナスとして使うもの
if len(A_pos) == 0:
    max_tmp = A_minus[-1]
    A_minus = A_minus[:-1]
    A_pos.append(max_tmp)

if len(A_minus) == 0:
    min_tmp = A_pos[0]
    A_pos = A_pos[1:]
    A_minus.append(min_tmp)

A_pos = deque(A_pos)
A_minus = deque(A_minus)

# calc steps
while True:
    if len(A_pos) == 1 and len(A_minus) == 1:
        break
    if len(A_pos) == 1:
        pos = A_pos.pop()
        minus = A_minus.pop()
        steps.append((pos, minus))
        pos -= minus
        A_pos.append(pos)
        continue
    if len(A_minus) == 1:
        # Then len(A_pos) > 1
        pos = A_pos.pop()
        minus = A_minus.pop()
        steps.append((minus, pos))
        minus -= pos
        A_minus.append(minus)
        continue
    pos = A_pos.pop()
    minus = A_minus.pop()
    steps.append((pos, minus))
    pos -= minus
    A_pos.append(pos)

pos = A_pos.pop()
minus = A_minus.pop()

steps.append((pos, minus))
print(pos - minus)
for x, y in steps:
    print('{} {}'.format(x, y))