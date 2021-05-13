X = open(0).read().split()[0]
ans = 0
s_count = 0
for x in X:
    if x == 'T':
        if s_count == 0:
            ans += 1
        else:
            s_count -= 1
    else:
        s_count += 1
print(ans+s_count)