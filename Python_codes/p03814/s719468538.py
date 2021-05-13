s=input()

#Aのインデックス
num_a=s.index("A")

#Zのインデックス
num_z=len(s)-1-s[::-1].index("Z")

print(num_z-num_a+1)