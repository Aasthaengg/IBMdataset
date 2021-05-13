s=input()
if len(s)==2:
    print(s)
else:
    for i in range(1,4):
        print(s[-i],end="")
    print()