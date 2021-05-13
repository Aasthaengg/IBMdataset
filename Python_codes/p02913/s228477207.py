N = int(input())
S = input()

def kAlgo(S, N):
    szS = N
    Z = [0]*szS
    Z[0] = szS
    i = 1 #current pos
    j = 0 #伸ばす幅
    while i < szS:
        while (i + j < szS) and (S[j] == S[i+j]): j += 1
        #set Z[i]
        Z[i] = j

        if j == 0:
            i += 1
            continue

        #optimize
        k = 1
        while (k < j) and (k + Z[k] < j):
            Z[i+k] = Z[k]
            k += 1

        i += k
        j -= k

    ans = 0
    for i in range(N):
        if Z[i] > i: Z[i] = i
    return max(Z[1:])

ans = 0
for i in range(N-1):
    lenz = kAlgo(S[i:], N-i)
    if ans < lenz:
        ans = lenz

print(ans)
