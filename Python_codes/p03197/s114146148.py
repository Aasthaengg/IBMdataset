import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = []
for i in range(n):
    lst1.append(int(readline()))

print("second" if all(i%2==0 for i in lst1) else "first")