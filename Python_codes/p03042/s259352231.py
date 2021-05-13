def main():
    s = input()
    #print(s[:2], s[2:4])
    if (int(s[:2]) > 12 or int(s[:2]) == 0)and (int(s[2:4]) >= 1 and int(s[2:4]) <= 12) :
        print("YYMM")
    elif (int(s[2:4]) > 12 or int(s[2:4]) == 0) and (int(s[:2]) >=1 and int(s[:2]) <=12) :
        print("MMYY")
    elif (int(s[:2]) >= 1 and int(s[:2])) <= 12 and (int(s[2:4]) >=1 and int(s[2:4]) <= 12) :
        print("AMBIGUOUS")
    else:
        print("NA")

if __name__ == "__main__":
    main()
