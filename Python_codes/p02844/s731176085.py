# D - Lucky PIN
N = int(input())
S = input()
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            tmp = 0
            while tmp<N and int(S[tmp])!=i:
                tmp += 1
            if tmp==N:
                continue
            tmp += 1
            while tmp<N and int(S[tmp])!=j:
                tmp += 1
            if tmp==N:
                continue
            tmp += 1
            while tmp<N and int(S[tmp])!=k:
                tmp += 1
            if tmp==N:
                continue
            ans += 1            
print(ans)