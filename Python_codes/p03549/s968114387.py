a,b = [int(i) for i in input().split()]

print((1900*b + 100*(a-b)) * 2**b)