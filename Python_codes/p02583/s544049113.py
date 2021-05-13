N = int(input())
l = list(map(int,input().split()))
ans = 0
if N < 3 :
    ans = ans
else :
    for m in range(N-2) :
        for n in range(m+1,N-1) :
            for k in range(n+1,N) :
                if len(set([l[m],l[n],l[k]])) == 3 and 2 * max(l[m],l[n],l[k]) < sum([l[m],l[n],l[k]]) :
                    ans += 1
                else :
                    continue
print(ans)