string = input()
l_idx = 0
r_idx = len(string) - 1
ans = 0
while l_idx <= r_idx:
    l = string[l_idx]
    r = string[r_idx]
    if l == r:
        l_idx += 1
        r_idx -= 1
    else:
        if l == 'x':
            l_idx += 1
            ans += 1
        elif r == 'x':
            r_idx -= 1
            ans += 1
        else:
            print(-1)
            exit()
print(ans)