n, m = map(int, input().split())
c = 1/pow(0.5, m)
print(int((100*(n-m)+1900*m)*c))