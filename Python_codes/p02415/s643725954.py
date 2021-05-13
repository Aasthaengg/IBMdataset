X = input()

for x in X:
    xx = x.upper()
    if x != xx:
        print(xx,end="")
    else:
        xxx = x.lower()
        if x != xxx:
            print(xxx,end="")
        else:
            print(x,end="")
print("")
