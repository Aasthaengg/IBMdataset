a, b, c = map(int, input().split())

s = (a+b+c)/2
S = s*(s-a)*(s-b)*(s-c)

print(int(S**0.5))