N = list(map(int,input().split()))
q = int(input())
S = []
S += [42,23,35,54],
S += [14,46,63,31],
S += [12,26,65,51],
S += [21,15,56,62],
S += [13,36,64,41],
S += [24,45,53,32],
for i in range(q):
    a,b = map(int,input().split())
    c = [str(N.index(a)+1)]
    c += str(N.index(b)+1),
    c = "".join(c)
    for j in range(6):
        if int(c) in S[j]:
            print(N[j])
