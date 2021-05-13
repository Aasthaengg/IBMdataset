import bisect

S = input()

R = []
L = []
for i,s in enumerate(S):
    if s=="R":
        R.append(i)
    else:
        L.append(i)

ans = [0]*len(S)    
for i,s in enumerate(S):
    if s=="R":
        l = bisect.bisect_left(L, i)
        if (L[l]-i)%2 == 1:
            ans[L[l]-1] += 1
        else:
            ans[L[l]] += 1
    else:
        r = bisect.bisect_left(R, i)-1
        if (i-R[r])%2 == 1:
            ans[R[r]+1] += 1
        else:
            ans[R[r]] += 1
            
print(*ans)