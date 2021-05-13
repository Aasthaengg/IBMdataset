AB,BC,CA=map(int,input().split())

ab=pow(AB,2)
bc=pow(BC,2)
ca=pow(CA,2)

if ab+bc==ca:
    print(int(AB*BC/2))
elif bc+ca==ab:
    print(int(BC*CA/2))
else:
    print(int(AB*CA/2))