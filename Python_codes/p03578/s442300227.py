N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

if M > N:
    print("NO")
    exit(0)

from collections import Counter
Dc = Counter(D)

for m in T:
    if m in Dc.keys():
        Dc[m] -= 1
        if Dc[m] < 0:
            print("NO")
            exit(0)
    else:
        print("NO")
        exit(0)

print("YES")