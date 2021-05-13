o = input()
e = input()
for i in range(len(o+e)):
    if i % 2 == 0:
        print(o[i//2],end="")
    else:
        print(e[(i-1)//2],end="")