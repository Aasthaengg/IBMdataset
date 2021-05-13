R,G,B,N = map(int,input().split())
ans = 0
for r in range(N+1):
    for g in range(N+1):
        num_box, amari = divmod(N-R*r-G*g, B)
        if num_box >= 0 and amari == 0:
            ans += 1
print(ans)