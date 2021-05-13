S = list(input())

length = len(S)
S.pop()
for _ in range(length):
    if len(S) % 2 != 0:
        S.pop()
        continue

    if S[:len(S)//2] == S[len(S)//2:]:
        print(len(S))
        break

    else:
        S.pop()
