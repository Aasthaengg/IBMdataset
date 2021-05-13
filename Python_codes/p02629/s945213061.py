N = int(input())
nameArr = []
chNum = 1

n = N - 1

while True:
    if n < 26*(26**chNum-1)//25:
        break
    chNum += 1

if chNum == 1:
    nameArr.append(n%26)
else:
    n = n - 26*(26**(chNum-1)-1)//25
    for i in range(chNum):
        nameArr.append(n//(26**(chNum-1-i)))
        n = n % (26**(chNum-1-i))

s = ""
for item in nameArr:
    if item == 0:
        s = s + "a"
    if item == 1:
        s = s + "b"
    if item == 2:
        s = s + "c"
    if item == 3:
        s = s + "d"
    if item == 4:
        s = s + "e"
    if item == 5:
        s = s + "f"
    if item == 6:
        s = s + "g"
    if item == 7:
        s = s + "h"
    if item == 8:
        s = s + "i"
    if item == 9:
        s = s + "j"
    if item == 10:
        s = s + "k"
    if item == 11:
        s = s + "l"
    if item == 12:
        s = s + "m"
    if item == 13:
        s = s + "n"
    if item == 14:
        s = s + "o"
    if item == 15:
        s = s + "p"
    if item == 16:
        s = s + "q"
    if item == 17:
        s = s + "r"
    if item == 18:
        s = s + "s"
    if item == 19:
        s = s + "t"
    if item == 20:
        s = s + "u"
    if item == 21:
        s = s + "v"
    if item == 22:
        s = s + "w"
    if item == 23:
        s = s + "x"
    if item == 24:
        s = s + "y"
    if item == 25:
        s = s + "z"

print(s)
