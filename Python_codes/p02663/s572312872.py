chr = input().split()
a = (int(chr[2]) - int(chr[0]))*60 + (int(chr[3]) - int(chr[1])) - int(chr[-1])
print(a)