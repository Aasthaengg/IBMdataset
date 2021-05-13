a,b=input().split()
d={"D":False,"H":True}
print("D" if d[a] ^ d[b] else "H")