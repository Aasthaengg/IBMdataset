D_kai, N_ban = map(int, input().split())

begin = 100 ** D_kai

if (N_ban == 100):
    ans = begin * 101
else:
    ans = begin * N_ban

print(ans)