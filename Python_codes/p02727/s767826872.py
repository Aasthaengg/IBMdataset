x,y,a,b,c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
ap = sorted(p)[a-x:]
aq = sorted(q)[b-y:]
r = sorted(r, reverse = True)

i,j,k = 0,0,0
flag = True

while k < c:
    if flag:
        if ap[i] <= aq[j]:
            if ap[i] <= r[k]:
                ap[i] = r[k]
                i += 1
                k += 1
                if i == x:
                    flag = False
                    continue
                continue
            else:
                break
        else:
            if aq[j] <= r[k]:
                aq[j] = r[k]
                j += 1
                k += 1
                if j == y:
                    flag = False
                    continue
                continue
    else:
        if i == x:
            if aq[j] <= r[k]:
                aq[j] = r[k]
                j += 1
                k += 1
                if j == y:
                    break
                continue
        else:
            if ap[i] <= r[k]:
                ap[i] = r[k]
                i += 1
                k += 1
                if i == x:
                    break
                continue
    
    break

ans = sum(ap) + sum(aq)
print(ans)
