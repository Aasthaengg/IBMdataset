n = int(input())
ab = []
for i in range(n):
    ai, bi = map(int,input().split())
    abi = [ai,bi]
    ab.append(abi)
sorted_ab = sorted(ab,key=lambda x : x[1])

fin = 0
for j in range(n):
    fin += sorted_ab[j][0]
    if fin > sorted_ab[j][1]:
        print("No")
        quit()
print("Yes")