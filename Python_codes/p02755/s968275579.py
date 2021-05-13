import sys
A, B = map(int, input().split())

for i in range(10000):
    a = int(i * 0.08)
    b = int(i * 0.1)
    if a == A and b == B:
        print(i)
        sys.exit()

print(-1)