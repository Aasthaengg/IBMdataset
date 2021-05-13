a = int(input())
if a<=6:
    print("1")
    exit()
if a<=11:
    print("2")
    exit()
if a%11==0:
    print(int(a/11)*2)
    exit()
if a%11<=6:
    print(int(a/11)*2+1)
else:
    print(int(a / 11) * 2 + 2)