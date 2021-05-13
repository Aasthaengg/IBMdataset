def main():
    a, b = input().split()

    liar = False
    if  a == "H" and b == "H" :
        liar = False
    elif a == "H" and b == "D" :
        liar = True
    elif a == "D" and b == "H" :
        liar = True
    elif a == "D" and b == "D" :
        liar = False
    
    if liar:
        print("D")
    else:
        print("H")

main()