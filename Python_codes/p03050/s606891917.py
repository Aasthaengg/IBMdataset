N = int(input())

l = []
for i in range(1, int(N**0.5)+1):
    if N%i==0:
        l.append(i)
        if i!=N//i:
            l.append(N//i)

ans = 0
for i in l:
    m = (N//i)-1
    if m:
        a, b = divmod(N, m)
        if a==b:
            ans += m

print(ans)