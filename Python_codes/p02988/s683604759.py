n = int(input())
p = list(map(int, input().split()))
cn = 0
for i in range(n - 2):
    if (p[i] < p[i+1] and p[i+1] < p[i+2]) or (p[i] > p[i+1] and p[i+1] > p[i+2]):
        cn = cn + 1
        
print(cn)