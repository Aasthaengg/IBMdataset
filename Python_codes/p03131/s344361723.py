k,a,b = [int(x) for x in input().split()]

l = k - (a - 1)

tmp = a + (b-a) * (l//2) + (l%2)
print(max(k+1, tmp))
