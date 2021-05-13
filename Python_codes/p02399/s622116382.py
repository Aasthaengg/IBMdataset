inps = input().split()
if len(inps) < 2:
    print("Illegal input.")
else:
    a = int(inps[0])
    b = int(inps[1])
    print("{} {} {:.10f}".format(a//b, a%b, a/b))