n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]
for h in range(n-m+1):
    for w in range(n-m+1):
        wi = [a[w:w+m] for a in A[h:h+m]]
        if wi == B:
            print('Yes')
            exit()
print('No')