S = input()
K = int(input())

if len(S) >= K and S[:K] == "1"*K:
    print(1)
else:
    for S in list(S):
        if S != "1":
            print(S)
            break