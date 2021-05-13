s = input()
tcd_g = s.count("g")
tcd_p = len(s) - tcd_g

acd_p = len(s)//2
acd_g = len(s) - acd_p

if tcd_g >= acd_p:
    print(acd_p - tcd_p)
else:
    print(tcd_g - acd_g)