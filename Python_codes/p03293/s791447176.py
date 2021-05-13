S = input()
T = input()
N = len(S)

for i in range(N):
    ref = ""
    ref = S[i:N] + S[0:i]
    if ref == T:
        print("Yes")
        break
else:
    print("No")
