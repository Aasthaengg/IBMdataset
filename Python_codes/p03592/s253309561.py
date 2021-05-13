n, m, k = map(int, input().split())
for nn in range(n+1):
    for mm in range(m+1):
        if nn*m+n*mm-2*nn*mm==k:
            print('Yes')
            break
    else:
        continue
    break
else:
    print('No')