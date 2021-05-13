N = int(input())
H = list(map(int, input().split()))
now = H[0]

for h in H:
    if h > now:
        now = h - 1
    elif h == now:
        continue
    else:
        print('No')
        exit()
print('Yes')