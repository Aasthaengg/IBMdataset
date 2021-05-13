s=input()

def month(n):
    if 1 <= n <= 12:
        return True
    else:
        return False


if int(s[0:2]) == 0:
    if month(int(s[2:4])) :
        print("YYMM")
        exit()
    else:
        print("NA")
        exit()

if int(s[2:4]) == 0:
    if month(int(s[0:2])):
        print("MMYY")
        exit()
    else:
        print("NA")
        exit()


if month(int(s[0:2])):
    if month(int(s[2:4])):
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if month(int(s[2:4])):
            print("YYMM")
    else:
        print("NA")
