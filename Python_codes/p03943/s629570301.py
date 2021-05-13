# https://atcoder.jp/contests/abc047/tasks/abc047_a
candy_packs = sorted(map(int, input().split()))
if candy_packs[2] == (candy_packs[0] + candy_packs[1]):
    print("Yes")
else:
    print("No")
