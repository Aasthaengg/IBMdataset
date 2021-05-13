n, r = list(map(int,input().strip().split()))
print(r + ((10-n)*100) if n < 10 else r) 