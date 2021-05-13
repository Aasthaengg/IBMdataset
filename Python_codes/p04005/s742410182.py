a, b, c = map(int, input().split())
abc = []
R, B = 0, 0
abc.append(a)
abc.append(b)
abc.append(c)
abc.sort()
R = abc[0] * abc[1] * (abc[2]//2)
B = a*b*c-R
print(B - R)