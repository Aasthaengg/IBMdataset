N = int(input())
S, T = input().split()

character = list()

for i in range(N):
    character.append(S[i])
    character.append(T[i])

answer = "".join(character)

print(answer)