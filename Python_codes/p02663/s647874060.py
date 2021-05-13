HMK = list(map(int, input().split()))
H1 = HMK[0]
M1 = HMK[1]
H2 = HMK[2]
M2 = HMK[3]
K = HMK[4]
if H2 < H1:
	H2 += 24
ans = ((H2 - H1) * 60 + (M2 - M1)) - K
print(ans)
