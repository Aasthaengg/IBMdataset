n=input()
h=len(n)
if h==1:
    print(int(n))
else:
    if n[1:]=="9"*(h-1):
        print(int(n[0])+9*(h-1))
    else:
        print(int(n[0])-1+9*(h-1))