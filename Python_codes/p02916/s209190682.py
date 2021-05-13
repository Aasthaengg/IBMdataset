N = int(input())
A_int_list = list(map(int, input().split()))
B_int_list = list(map(int, input().split()))
C_int_list = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += B_int_list[A_int_list[i] - 1]
    if i != N - 1 and A_int_list[i] + 1 == A_int_list[i + 1]:
        ans += C_int_list[A_int_list[i] - 1]

print(ans)
