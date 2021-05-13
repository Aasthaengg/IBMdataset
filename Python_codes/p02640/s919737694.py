X,Y=map(int, input().split())
for a in range(X+1):
    if 2*a+4*(X-a)==Y:
        print ("Yes")
        exit()
    else:
        continue
print("No")