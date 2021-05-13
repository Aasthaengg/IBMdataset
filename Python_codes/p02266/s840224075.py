import collections
import sys

S1 = collections.deque()
S2 = collections.deque()

for i, j in enumerate(sys.stdin.readline()):
    if j == '\\':
        S1.append(i)
    elif j == '/':
        if S1:
            left_edge = S1.pop()
            new_puddle = i - left_edge
            while S2 and (S2[-1][0] > left_edge):
                new_puddle += S2[-1][1]
                S2.pop()
            S2.append((left_edge, new_puddle))
        else:
            pass


print(sum(j for i, j in S2))

print(len(S2), *(j for i, j in S2))