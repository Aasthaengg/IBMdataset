N = int(input())
c_range = -(-N // 4) + 1
d_range = -(-N // 7) + 1
for d in range(d_range):
    for c in range(c_range):
        if c * 4 + d * 7 == N:
            print('Yes')
            break
    else:
        continue
    break
else:
    print('No')
