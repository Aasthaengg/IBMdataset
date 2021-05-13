from collections import Counter
H, W = map(int, input().split())
count = Counter()
for _ in range(H):
    s = input()
    for j in range(W):
        count[s[j]] += 1
four = int(H/2) * int(W/2)
two = (H%2)*int(W/2) + (W%2)*int(H/2)
one = (H%2) * (W%2)
# print(count)
# print(four, two, one)
for i in range(26):
    alpha = chr(ord("a")+i)
    # 4つ組を使えるかどうか
    while count[alpha] >= 4 and four > 0:
        count[alpha] -= 4
        four -= 1
    while count[alpha] >= 2 and two > 0:
        count[alpha] -= 2
        two -= 1
    while count[alpha] >= 1 and one > 0:
        count[alpha] -= 1
        one -= 1
if four == two == one == 0:
    print("Yes")
else:
    print("No")
