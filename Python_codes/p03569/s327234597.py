S = input()
N = len(S)
L = list(S)
left_idx = 0
right_idx = N - 1
ret = 0
while left_idx < right_idx:
    l = S[left_idx]
    r = S[right_idx]
    if l == r:
        left_idx += 1
        right_idx -= 1
    elif l == "x":
        ret += 1
        left_idx += 1
    elif r == "x":
        ret += 1
        right_idx -= 1
    else:
        ret = -1
        break

print(ret)
