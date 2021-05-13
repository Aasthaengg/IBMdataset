from math import sqrt
N=int(input())
q=int(sqrt(N*2))
if N*2!=q*q+q:print("No")
else:
    S=[list(range(1,q+1))]
    for j in range(1,q+1):S.append([j])
    last = q
    for i in range(1,q):
        r = list(range(last+1,last+1+q-i))
        S[i] += r
        for j in range(q-i):
            S[i+j+1] += [r[j]]
        last = r[-1]
    print("Yes")
    print(len(S))
    for s in S: print(len(s), " ".join(str(i)for i in s))