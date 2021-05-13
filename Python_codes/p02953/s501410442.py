_ = int(input())
H = list(map(int, input().split()))

ans = 'Yes'
last_h = H[-1]
for h in reversed(H):
    if h - last_h > 1:
        ans = 'No'
        break
    elif h - last_h == 1:
        last_h = h - 1
    else:
        last_h = h

print(ans)