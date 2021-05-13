n = int(input())
sn = str(n)
k = len(sn)
c = int(sn[0])
if sn == str(c) + "9" * (len(sn) - 1):
    print(c + 9 * (k - 1))
else:
    print(c + 9 * (k - 1) - 1)
