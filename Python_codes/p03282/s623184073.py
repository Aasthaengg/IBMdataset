S = input()
K = int(input())
for i, c in enumerate(S, 1):
    if c != "1":
        print(c)
        break
    if i == K:
        print(1)
        break