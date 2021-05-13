x, k = map(int, input().split())
print(*(i for i in range(k-x+1, k+x)), end= ' ')