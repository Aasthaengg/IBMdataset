n = int(input())
s = [0] + list(map(int, input().split()))
s.append(0)
forward = []
backward = []
jump = []
for a, b, c in zip(s, s[1:], s[2:]):
    forward.append(abs(b - a))
    backward.append(abs(c - b))
    jump.append(abs(c - a))
res = sum(forward) + backward[-1]
for i in range(n):
    print(res + jump[i] - forward[i] - backward[i])
