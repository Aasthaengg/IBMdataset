S = input()
q = int(input())

for idx in range(q):
    e = input().split()
    a = int(e[1])
    b = int(e[2])

    if e[0] == "print":
        print(S[a:b+1])
    elif e[0] == "reverse":
        SS = S[a:b+1]
        S = S[:a] + SS[::-1] + S[b+1:]
    elif e[0] == "replace":
        S = S[:a] + e[3] + S[b+1:]

