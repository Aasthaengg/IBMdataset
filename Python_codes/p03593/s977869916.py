import sys
from collections import Counter

H, W = map(int, sys.stdin.readline().split())

string = ""
for _ in range(H):
    string += sys.stdin.readline().strip()

counter = Counter(string)
e_one = 0
e_two = 0
e_four = 0
for key, count in counter.items():
    tmp = count // 4
    e_four += tmp
    count -= 4 * tmp
    tmp = count // 2
    e_two += tmp
    count -= 2 * tmp
    e_one += count

four = (H//2) * (W//2)
two = (H%2) * (W//2) + (H//2) * (W%2)
one = (H%2) * (W%2)

# print("exists", e_four, e_two, e_one)
# print("needs", four, two, one)

if four > e_four:
    print("No")
else:
    e_four -= four
    e_two += e_four * 2
    if two > e_two:
        print("No")
    else:
        e_two -= two
        e_one += e_two * 2
        if e_one == one:
            print("Yes")
        else:
            print("No")