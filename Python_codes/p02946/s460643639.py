k,x = map(int, input().split())

a = max(-1000000,x - (k-1))
b = min(1000000,x+(k-1))

L = [str(i) for i in range(a,b+1)]
print(" ".join(L))
