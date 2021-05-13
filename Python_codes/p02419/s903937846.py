T = ""
W = input().casefold()
while True:
    tmp = input()
    if tmp == "END_OF_TEXT":
        break
    T += tmp + " "
print(sum([1 for c in T.split() if c.casefold() == W]))