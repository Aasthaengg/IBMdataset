n,m,d = map(int, input().split())

print((n-d)*(m-1)*2/n/n if d!=0 else (n-d)*(m-1)/n/n)