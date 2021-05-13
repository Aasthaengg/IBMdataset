n = [int(input()) for _ in range(4)]
if n[0]<=n[1]:
    print(n[0]*n[2])
else:
    print((n[1]*n[2])+(n[0]-n[1])*n[3])