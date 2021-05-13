k,x = map(int, input().split())
print(" ".join(list(map(str, list(range(x-k+1, x+k))))))