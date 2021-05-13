o=input()
e=input()
if len(o)==len(e):
    for i in range(int(len(o))):
        print(o[i],end="")
        print(e[i],end="")
else:
    for i in range(int(len(e))):
        print(o[i],end="")
        print(e[i],end="")
    print(o[-1:])