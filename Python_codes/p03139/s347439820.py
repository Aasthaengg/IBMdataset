n,a,b = [int(i) for i in input().split()]

print(min(a,b), a+b-n if a+b-n > 0 else 0)