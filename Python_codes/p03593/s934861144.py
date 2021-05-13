from collections import Counter


def solve():
    YES, NO = "Yes", "No"
    if H % 2 and W % 2:
        if rems[1] == 0 and rems[3] == 1:
            rems[1] += 1
            rems[2] += 1
            rems[3] = 0
        if rems[1] != 1 or rems[3] or rems[2] > H // 2 + W // 2:
            return NO
        else:
            return YES
    elif H % 2 or W % 2:
        even_edge = H if W % 2 else W
        if rems[1] + rems[3] or rems[2] > even_edge // 2:
            return NO
        else:
            return YES
    else:
        if rems[1] + rems[2] + rems[3]:
            return NO
        else:
            return YES


H, W = map(int, input().split())
c = Counter()
for _ in range(H):
    c += Counter(input())
rems = Counter(v % 4 for v in c.values())
print(solve())
