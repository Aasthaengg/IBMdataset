S = input()

answer = "".join([c for i, c in enumerate(S) if (i+1) % 2 == 1])
print(answer)