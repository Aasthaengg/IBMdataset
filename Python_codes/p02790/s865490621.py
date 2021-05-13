a,b = map(int,input().split())
min_a=str(a)*b
min_b=str(b)*a
print(min(min_a, min_b))