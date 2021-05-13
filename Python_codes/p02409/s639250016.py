# ITP1_6_C
# Array - Official House
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_C&lang=jp
from sys import stdin

n = int(stdin.readline().rstrip())

NUMBER_OF_BUILDING = 4
FLOORS_PER_BUILDING = 3
ROOMS_PER_FLOOR = 10

official_house = [
    [
        [
            0 for _ in range(ROOMS_PER_FLOOR)
            ] for _ in range(FLOORS_PER_BUILDING)
        ] for _ in range(NUMBER_OF_BUILDING)
    ]

for cnt in range(n):
    b, f, r, v = (int(n) for n in stdin.readline().rstrip().split())
    official_house[b - 1][f - 1][r - 1] += v

for no, building in enumerate(official_house):
    if no != 0:
        print("#" * 20)

    for floor in building:
        print(" " + " ".join(map(str, floor)))

