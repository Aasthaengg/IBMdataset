N = int(input())
ans = 0
for i in range(1,N+1):
    ans += (N//i)*(i+(i*(N//i)))//2
print(ans)