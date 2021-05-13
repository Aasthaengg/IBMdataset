x = int(input())

ans = False
for a in range(-10**3,10**3):
    for b in range(-10**3,10**3):
        if a**5 - b**5 == x:
            print(a,b)
            ans = True
            break
    if ans:
        break
