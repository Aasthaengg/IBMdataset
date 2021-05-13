import sys

for in_str in sys.stdin:
#    comp_list = list(map(int, in_str.split(" ")))
    a, b = map(int, in_str.split())
    #a = comp_list[0]
    #b = comp_list[1]
    if (a == 0) & (b == 0) : break
    elif a < b :
        print(a, b)
    else :
        print(b, a)