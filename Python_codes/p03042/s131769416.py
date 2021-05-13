s = input()
v=0
for i in range(4):
    v = v*10+int(s[i])
v1 = v//100
v2 = v%100
if 12>=v1>=1 and 12>=v2>=1:
    print("AMBIGUOUS")
elif (v1>=13 or v1==0) and 12>=v2>=1:
    print("YYMM")
elif (v2>=13 or v2==0) and 12>=v1>=1:
    print("MMYY")
else:
    print("NA")