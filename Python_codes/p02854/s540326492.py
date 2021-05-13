N = int(input())
la = list(map(int, input().split()))

S = sum(la)
lsum = 0
i = 0
while lsum < S/2:
    lsum += la[i]
    i += 1

sm = min(lsum , lsum-la[i-1])

if lsum - S/2 > S/2 - (lsum-la[i-1]):
    print(S - 2*(lsum-la[i-1]))
else:
    print(2*lsum - S)