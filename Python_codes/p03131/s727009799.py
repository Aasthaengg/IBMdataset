K,A,B = list(map(int,input().split()))
if B-A <= 1:
    print(K+1)
    exit()
ans = A
K = K - (A-1)
yen = 0
if K%2 == 0:
    ans += (B-A)*(K//2)
else:
    ans += (B-A)*(K//2)+1
print(ans)