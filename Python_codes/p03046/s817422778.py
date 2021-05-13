import sys

m, k = map(int, raw_input().split(" "))

if k >= 2 ** m:
    print(-1)
    sys.exit(0)

if m == 0:
    if k == 0:
        print("0 0")
        sys.exit(0)

    else:
        print(-1)
        sys.exit(0)

if m == 1:
    if k == 0:
        print("0 1 1 0")
        sys.exit(0)

    else:
        print(-1)
        sys.exit(0)


for i in range(0, 2 ** m):
    if i != k:
        sys.stdout.write("%d " % i)

sys.stdout.write("%d " % k)

for i in range((2 ** m) -1, 0 - 1, -1):
    if i != k:
        sys.stdout.write("%d " % i)

print(k)
