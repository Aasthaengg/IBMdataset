N_all, M_part = map(int, input().split())

time = 1900 * M_part + 100 * (N_all - M_part)
ans = 2 ** M_part * time

print(ans)