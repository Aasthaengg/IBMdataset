n, m = sorted(map(int, input().split()))
print(1 if n==m==1 else m-2 if n==1 else (n-2)*(m-2))