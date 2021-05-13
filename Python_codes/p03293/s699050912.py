S = input()
T = input()

for _ in range(len(S)):
    S = S[-1] + S[:-1]
    if T == S:
        print("Yes")
        exit(0)

else:
    print("No")