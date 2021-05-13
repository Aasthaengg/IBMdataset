inputs = list(map(str,input().split()))
a=int(inputs[0])
b=int(inputs[2])
if inputs[1]=="-":
    print(a-b)
else:
    print(a+b)