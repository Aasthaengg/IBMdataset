n = int(input())
cn = [0 for i in range(n+1)]
for i in range(n):
    p = int(input())
    cn[p] = cn[p-1]+1

print(n-max(cn))
