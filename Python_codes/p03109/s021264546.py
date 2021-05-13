s = input()
a = int(s[:4])
b = int(s[5:7])
c = int(s[8:])
n = a * 10000 + b * 100 + c
if n <= 20190430:
    print("Heisei")
else:
    print("TBD")
