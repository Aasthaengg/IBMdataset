P, Q, R = map(int, input().split())

a = P + Q
b = Q + R
c = P + R
l = [a, b, c]
print(min(l))
