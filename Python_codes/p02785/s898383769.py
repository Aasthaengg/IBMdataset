import sys
input = sys.stdin.readline

(n, k), s, c = map(int, input().split()), sorted(list(map(int, input().split())), reverse = True), 0
for i in range(n-k): c += s.pop()
print(c)