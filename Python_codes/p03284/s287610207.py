N_mai, K_nin = map(int, input().split())

if (N_mai % K_nin == 0):
    ans = 0
else:
    ans = 1

print(ans)