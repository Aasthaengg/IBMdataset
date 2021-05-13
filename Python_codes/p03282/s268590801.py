S = input()
K = int(input())
judge = 1

for i in range(K):
    if S[i] != "1":
        print(S[i])
        judge = 0
        break

if judge != 0:
    print("1")