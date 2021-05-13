import itertools

H, W, K = map(int, input().split())
C = []
 
for i in range(H):
    C.append(input())

ans = 0

for i in range(H+1):
    for j in range(W+1):
        for m in itertools.combinations(list(range(H)), i):
            for n in itertools.combinations(list(range(W)), j):
                count = 0
                for a in m:
                    for b in n:
                        if(C[a][b] == "#"):
                            count += 1
                if(count == K):
                    ans += 1

print(ans)
