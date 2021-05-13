a=int(input())
print(a/2/a if a%2 == 0 else ((a-1)/2+1)/a)