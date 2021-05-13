a,b,c = input().split()
print('YNEOS'[not(a[-1] == b[0] and b[-1]==c[0])::2])