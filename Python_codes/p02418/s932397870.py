s = input()
p = input()

S = s+s

index = S.find(str(p))

if index != -1:
    print ("Yes")
else:
    print("No")