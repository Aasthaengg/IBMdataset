n = int(input())

P = [0]
p = 1
for i in range(10**3):
    P.append(P[-1] + p)
    p += 1

i = 1
while P[i] < n:
    i += 1
if P[i] > n:
    print("No")
else:
    print("Yes")
    m = i+1
    S = [[] for i in range(m)]
    for i in range(m):
        s = 1 if i==0 else 1+P[i-1]
        for j in range(m-1):
            S[i].append(s)
            if j < i-1:
                s += 1
            elif j == i-1:
                s += i+1
            else:
                s += j+1
    print(m)
    for i in range(m):
        print(m-1, " ".join([str(j) for j in S[i]]))

# print(S)