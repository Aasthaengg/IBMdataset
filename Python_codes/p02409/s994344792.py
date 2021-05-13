import sys

data = [0] * (4 * 3 * 10)

def get_index(b, f, r):
    return ((b - 1) * 3 + (f - 1)) * 10 + (r - 1)

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    data[get_index(b, f, r)] += v

for b in range(1, 5):
    for f in range(1, 4):
        for r in range(1, 11):
            sys.stdout.write(" %d" % data[get_index(b, f, r)])
        sys.stdout.write("\n")
    if b != 4:
        print("#" * 20)