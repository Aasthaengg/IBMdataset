origin = [ "", "KIH", "", "B", "", "R", "" ]

candidate = []
for i in range(2**4):
    temp = [ j for j in origin ]
    bit = bin(i)[2:].zfill(4)
    for j, v in enumerate(bit):
        if v == "1":
            temp[2*j] = "A"
    candidate.append("".join(temp))

s = input()
print( "YES" if s in candidate else "NO" )