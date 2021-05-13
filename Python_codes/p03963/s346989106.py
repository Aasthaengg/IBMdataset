n, k = (int(x) for x in input().split())
print(k*((k-1)**(n-1))) if n != 1 else print(k)