k,x = map(int, input().split())
l = [str(y) for y in range(x-k+1,x+k)]
print(" ".join(l))