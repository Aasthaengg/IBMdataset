s =  list(input())
if ("C" in s and "F" in s):
    if(s.count("F") == 1):
        if(s.index("C") < s.index("F")):
            print("Yes")
        else:
            print("No")
    else:
        if(s.index("C") < s.index("F",1)):
            print("Yes")
        else:
            print("No")

else:
    print("No")