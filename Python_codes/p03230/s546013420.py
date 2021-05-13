N = int(input())

n = int((2*N)**0.5)
if n*(n+1) == 2*N:
    print("Yes")
    print(n+1)
    S = [[] for _ in range(n+1)]
    num = 1
    for i in range(n+1):
        j = i+1
        while len(S[i]) < n:
            S[i].append(str(num))
            S[j].append(str(num))
            num += 1
            j += 1
    for i in range(n+1):
        print(n, " ".join(S[i]))
    
else:
    print("No")