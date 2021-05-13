N = int(input())
L = [int(i)for i in input().split()]
ans = 0
L.sort(reverse=True)
for i,l in enumerate(L[:-2]):
    for j,l2 in enumerate(L[i+1:N-1]):
        for l3 in L[i+j+2:]:
            if l < l2 + l3:
                if l > l2 > l3:
                    ans += 1
            else:
                break
print(ans)