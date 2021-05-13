H, W = map(int, input().split(" "))
four, two, one = 0, 0, 0

four += ((H // 2)) * (W // 2)
if W % 2 == 1:
    two += (H // 2)
if H % 2 == 1:
    two += (W // 2)

one += (H * W) % 2

counter = {}
for _ in range(H):
    A = input()
    for a in A:
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1

flag = True
for c in counter:
    if counter[c] >= 4 and four > 0:
        mk_four = min(four, counter[c] // 4)
        four -= mk_four
        counter[c] -= mk_four * 4
    if counter[c] >= 2 and two > 0:
        mk_two = min(two, counter[c] // 2)
        two -= mk_two
        counter[c] -= mk_two * 2
    if counter[c] >= 1 and one > 0:
        mk_one = min(one, counter[c])
        one -= mk_one
        counter[c] -= mk_one

    if counter[c] != 0:
        flag = False


if flag and (four == two == one == 0):
    print('Yes')
else:
    print('No')