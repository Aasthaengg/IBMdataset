a, b, c, d = map(int, input().split())

l = [a*c, a*d, b*c, b*d]
maxNum = max(l)

print(maxNum)