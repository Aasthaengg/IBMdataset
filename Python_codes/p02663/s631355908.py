h1,h2,h3,h4,k = map(int,input().split())
h11 = h1 * 60 + h2
h22 = h3 * 60 + h4
print(h22-h11-k)
