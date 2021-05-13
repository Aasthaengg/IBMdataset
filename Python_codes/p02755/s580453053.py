##############################################
import sys
A, B = list(map(int, input().split()))
for i in range(1,1009+1):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        sys.exit(0)

print(-1)
