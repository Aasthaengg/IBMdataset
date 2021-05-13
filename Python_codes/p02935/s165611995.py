N = int(input())
v_int_list = list(map(int, input().split()))
v_int_list = sorted(v_int_list)

ans = v_int_list[0]
for i in range(1, N):
    ans = (ans + v_int_list[i]) / 2

print(ans)
