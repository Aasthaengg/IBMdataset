import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w, a, b = map(int, readline().split())
ans_1 = '1' * a + '0' * (w - a)
ans_2 = '0' * a + '1' * (w - a)
for i in range(b):
    print(ans_1)
for i in range(h - b):
    print(ans_2)
