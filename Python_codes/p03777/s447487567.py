a,b=input().split()
hatsugen=["H","D"]
idx=hatsugen.index(b)
if a=="H":
    print(hatsugen[idx])
else:
    print(hatsugen[1-idx])