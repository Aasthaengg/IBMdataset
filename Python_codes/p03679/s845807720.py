input = input()
s_input = input.split()
x = int(s_input[0])
a = int(s_input[1])
b = int(s_input[2])

kigenchouka = b - a

if kigenchouka > x:
    print("dangerous")
else:
    if kigenchouka <= 0:
        print("delicious")
    else:
        print("safe")
