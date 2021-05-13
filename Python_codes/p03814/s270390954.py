s = input()
amin = 10000000000
amax = -1

for i, j in enumerate(s):
    if j=="A":
        amin = min(amin, i)
    elif j=="Z":
        amax = max(amax, i)
    
print(amax-amin+1)