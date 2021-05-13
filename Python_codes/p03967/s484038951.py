s=input()
g=s.count("g")
p=s.count("p")
length=len(s)
if g-p<2:
    print(0)
else:
    print(abs(p - length//2 ))