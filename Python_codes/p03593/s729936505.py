from collections import Counter

H, W = map(int, input().split())

raw = ""
for i in range(H):
    raw = raw + input()
words = Counter(list(raw))

if H*W % 2 == 1:
    flag = 0
    two_sum = (H-1) + (W-1)
elif H%2 == 1:
    flag = 1
    two_sum = W
elif W%2 == 1:
    flag = 1
    two_sum = H
else:
    flag = 1
    two_sum = 0

for value in words.values():
    if value % 2 == 1:
        flag += 1
    if flag > 1:
        print("No")
        break

if flag < 2 and two_sum > -1:
    for key, value in words.items():
        N_key = value
        while N_key > 0:
            if 1 < N_key < 4:
                N_key -= 2
                two_sum -= 2
            else:
                N_key -= 4

if flag < 2 and two_sum > -1:
    print("Yes")
elif two_sum < 0:
    print("No")
