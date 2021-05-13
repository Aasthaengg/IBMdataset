n = int(input())

waru = int(n**0.5)
while True:
    if n%waru == 0:
        a = waru
        b = n//waru
        break
    else:
        waru -= 1
print(a+b-2)
