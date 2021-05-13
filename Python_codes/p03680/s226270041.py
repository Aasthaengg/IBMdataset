n = int(input())
nxt_btn = {i: int(input()) for i in range(1, n + 1)}

num = -1
crr_btn = 1
for i in range(1, n + 1):
    if nxt_btn[crr_btn] == 2:
        num = i
        break
    crr_btn = nxt_btn[crr_btn]
print(num)
