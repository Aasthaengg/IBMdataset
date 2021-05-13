n,k,l = (int(x) for x in input().split())

out = n+k+l
out -= max(n,k,l)

print(out)