n = int(input())
A = list(map(int,input().split()))
B = A[:]
cntp = 0
totp = 0
for i in range(n):
    if i%2==0:
        if B[i]>=1-totp:
            totp += B[i]
        else:
            cntp += 1-totp-B[i]
            totp = 1
    else:
        if B[i]<=-1-totp:
            totp += B[i]
        else:
            cntp += B[i]+1+totp
            totp = -1
cntm = 0
totm = 0
for i in range(n):
    if i%2==0:
        if B[i]<=-1-totm:
            totm += B[i]
        else:
            cntm += B[i]+1+totm
            totm = -1
    else:
        if B[i]>=1-totm:
            totm += B[i]
        else:
            cntm += 1-totm-B[i]
            totm = 1
print(min(cntp,cntm))