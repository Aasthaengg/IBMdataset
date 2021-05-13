cubic = list(map(int, input().split()))
sort_cubic = sorted(cubic, reverse=True)
a = sort_cubic[0]
b = sort_cubic[1]
c = sort_cubic[2]
red = (a // 2 ) * b * c
blue = (a - a//2) * b * c
print(abs(red - blue))
