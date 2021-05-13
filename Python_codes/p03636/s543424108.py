s=input()

fir=s[0]
las=s[-1]

s=s[1:]
s=s[:-1]

print(fir+str(len(s))+las)