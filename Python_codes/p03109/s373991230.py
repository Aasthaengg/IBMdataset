s = list(input())
del s[7]
del s[4]
print("Heisei" if int(''.join(s)) <= 20190430 else "TBD")
