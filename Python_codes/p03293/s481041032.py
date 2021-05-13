S = list(input())
T = list(input())

for _ in range(len(S) + 1):
    if S == T:
        print("Yes")
        break
    S.append(S.pop(0))
else:
    print("No")