import sys
N = int(input())
p = list(map(int, input().split()))
q = sorted(p)

count = 0
for i, j in zip(p, q):
    if i != j:
        count += 1
        if count > 2:
            print("NO")
            sys.exit()
print("YES")


