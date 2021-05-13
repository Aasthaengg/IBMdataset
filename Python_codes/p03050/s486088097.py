N = int(input())

ans = 0
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        d = i-1
        if d!=0 and N//d==N%d:
            ans += d
        if i*i!=N:
            d = N//i-1
            if d!=0 and N//d==N%d:
                ans += d

print(ans)