S = input()
K = int(input())

for i, s in enumerate(S, 1):
    if s != "1":
        print(s)
        break
    else:
        if i == K:
            print("1")
            break