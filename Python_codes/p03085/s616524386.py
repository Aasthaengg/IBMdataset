pair1 = ["A","T"]
pair2 = ["G","C"]

b = input()

if b in pair1:
    pair1.remove(b)
    print(pair1[0])
    
else:
    pair2.remove(b)
    print(pair2[0])