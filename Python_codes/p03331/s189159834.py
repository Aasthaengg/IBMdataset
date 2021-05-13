N = int(input())
ans = 10**14
for i in range(1, N//2+1):
    a = sum(map(int, str(i)))
    b = sum(map(int, str(N-i)))
    ans = min(a+b, ans)
print(ans)