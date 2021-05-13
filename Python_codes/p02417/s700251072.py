import sys
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
C = []
b = ""
for line in sys.stdin:
    a = line.lower()
    b += a
for i in range(len(alpha)):
    k = b.count(alpha[i])
    C.append(k)
for i in range(len(alpha)):
    print(alpha[i]+" :",C[i])
