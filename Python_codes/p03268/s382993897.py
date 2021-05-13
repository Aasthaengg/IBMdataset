n, k = map(int, input().split())

if k%2 == 0:
    q1, r1 = divmod(n, k)
    if r1 < k//2:
        q2 = q1
    else:
        q2 = q1+1
    ans = q2**3 + q1**3
else:
    q1, r1 = divmod(n, k)
    ans = q1**3
#print(q1, q2)
print(ans)
