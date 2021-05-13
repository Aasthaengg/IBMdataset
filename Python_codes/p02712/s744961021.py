N = int(input())

Ndiv3 = N // 3
Ndiv5 = N // 5
Ndiv15 = N // 15

ans = (N*(N + 1) - 3*Ndiv3*(Ndiv3 + 1) - 5*Ndiv5*(Ndiv5 + 1) + 15*Ndiv15*(Ndiv15 + 1))//2
print(ans)