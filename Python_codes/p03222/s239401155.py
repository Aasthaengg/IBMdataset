
H,W,K = map(int,input().split())

amari = [1,1,2,3,5,8,13,21]

lis = [0] * W

lis[0] += 1

for j in range(H):

    nlis = [0] * W

    for i in range(W):

        if i > 0:

            if i == 1:
                nlis[i-1] += lis[i] * amari[W-2]

            else:
                nlis[i-1] += lis[i] * amari[i-1] * amari[W-1-i]

        nlis[i] += lis[i] * amari[i] * amari[W-1-i]

        if i < W-1:

            if i == W-2:
                nlis[i+1] += lis[i] * amari[W-2]

            else:
                nlis[i+1] += lis[i] * amari[i] * amari[W-i-2]

    for i in range(W):

        lis[i] = nlis[i] % (10 ** 9+ 7)

print (lis[K-1] % (10**9 + 7))
