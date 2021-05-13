S = input()
num = S.count("x")
if 1 <= len(S) <= 15:
    if 1 <= len(S) <= 7 :
        print("YES")
    else :
        if num >= 8 :
            print("NO")
        else :
            print("YES")
