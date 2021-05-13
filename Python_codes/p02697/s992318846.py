n, m = map(int, input().split())
for i in range(m):
    if i % 2 == 0:
        print(i//2+1, (n-1)//2-i//2+1)
    else:
        print(n-(n-1)//2+i//2+1, n-i//2)