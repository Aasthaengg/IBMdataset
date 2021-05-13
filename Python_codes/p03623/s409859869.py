x, a, b = map(int,input().split())
print("AB"[(x*2 > a+b)^(a>b)])