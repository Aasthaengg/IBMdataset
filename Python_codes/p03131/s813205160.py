K,A,B = map(int,input().split())
if B<=A+2 or K<=A-1:
    ans = 1+K
else:
    cnt = A-1
    ans = A
    while cnt<=K:
        k = min(ans//A,(K-cnt)//2)
        if k>=1:
            cnt += 2*k
            ans = ans-k*A + k*B
        else:
            ans += (K-cnt)
            break
print(ans)