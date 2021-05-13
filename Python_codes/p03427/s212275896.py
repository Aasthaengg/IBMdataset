N = int(input())
keta = len(str(N))
SN = str(N)
if N <= 9:
    print(N)
elif SN.count('9') == keta:
    print(9*keta)
elif SN.count('9') == keta-1 and SN[0] != '9':
    print((keta - 1) * 9 + int(SN[0]))
else:
    print((keta - 1) * 9 + int(SN[0])-1)