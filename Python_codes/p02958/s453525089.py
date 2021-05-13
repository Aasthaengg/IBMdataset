import sys

N = int(sys.stdin.readline())
ps = [int(x) for x in sys.stdin.readline().split(" ")]


wrong_count = 0
for i in range(0, N):
    if ps[i] == i + 1:
        continue
    wrong_count += 1

if wrong_count == 0 or wrong_count == 2:
    print("YES")
else:
    print("NO")
