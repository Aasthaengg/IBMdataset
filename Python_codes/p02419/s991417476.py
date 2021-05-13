import sys
w = sys.stdin.readline().strip().lower()
t = sys.stdin.read().lower().split()[:-1]
print(t.count(w))