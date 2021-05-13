a,b,c = map(int, input().split())
print(min(a*b//2, b*c//2, c*a//2))