h, a= map(int, input().split(" "))
r = h // a
remainder = h % a
while remainder > 0:
    remainder -= a
    r += 1

print(r)