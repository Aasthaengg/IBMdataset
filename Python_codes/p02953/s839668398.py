N = int(input())
H = list(map(int, input().split()))

ans = 'Yes'
tmp_max = H[-1]

for h in reversed(H[:-1]):
    if h <= tmp_max:
        tmp_max = h
    elif h-1 <= tmp_max:
        tmp_max = h-1
    else:
        ans = 'No'

print(ans)
