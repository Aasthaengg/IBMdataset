args = str(input())
args = args.split(" ")
a = int(args[0])
b = int(args[1])
k = int(args[2])

turn = 0
for i in range(k):
    if (turn==0):
        if (a>0):
            if (a % 2 == 1):
                a = a - 1
        if (a>0):
            g = a/2
            a = a - g
            b = b + g
        turn=1
    elif (turn==1):
        if (b>0):
            if (b % 2 == 1):
                b = b -1
        if (b>0):
            g = b/2
            b = b - g
            a = a + g
        turn=0

print(int(a),int(b))
