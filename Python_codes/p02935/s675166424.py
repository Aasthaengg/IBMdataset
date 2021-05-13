import collections
n = int(input())
v = collections.deque(sorted(list(map(int, input().split()))))

while len(v) > 1:
    x = (v.popleft()+v.popleft())/2
    v.append(x)
    v = collections.deque(sorted(list(v)))
print(v[0])
