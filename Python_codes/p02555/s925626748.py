s = int(input())
C = [1]
for n in range(1, s+1): C.append(sum(C[:n-3+1]) % (10**9 + 7)) # sum(C[0,n-3])
print(C[s])
