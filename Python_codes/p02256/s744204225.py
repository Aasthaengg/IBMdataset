a, b = map(int, input().split())

if a < b:
    t = a
    a = b
    b = t
while b != 0 and b <= a:
    t = a % b
    a = b
    b = t

print(a)