n, k = list(map(int , input().split()))
q,mod = divmod(n,k)
if mod == 0:
    print(0)
else:
    print(1)