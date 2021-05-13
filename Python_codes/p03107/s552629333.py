S = list(input())

blue = S.count('1')
red = S.count('0')

print(len(S) - abs(blue - red))