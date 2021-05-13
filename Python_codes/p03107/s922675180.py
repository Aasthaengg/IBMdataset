s = list(input())
one  = s.count("1")
zero = s.count("0")
if(one == 0 or zero == 0):
    print("0")
else:
    if (one > zero):
        print(zero * 2)
    else:
        print(one * 2)
