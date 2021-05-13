import sys

*N, = set(map(int, input().split()))

l = [1,9,7,4]

for i in range(len(l)):
    if not (l[i] in N):
        print("NO")
        sys.exit()

print("YES")