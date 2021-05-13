A, B = map(int,input().split())

a = A + B
b = A - B
c = A * B
l = [a, b, c]
l.sort(reverse=True)
print(l[0])
