N = int(input())
c = (N+1)//2
ans = 0
for i in range(1,N-c+1):
    ans += i*(1+N//i)*(N//i)/2
ans += N*c -(c-1)*c/2
print(int(ans))