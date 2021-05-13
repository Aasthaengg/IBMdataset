H = int(input())
r = 0
for i in range(41):
    if H < 2**i:
        print(r)
        break
    r += 2**i
