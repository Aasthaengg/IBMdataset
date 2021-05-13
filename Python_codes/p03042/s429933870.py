def main():
    s=input()
    s1=int(s[:2])
    s2=int(s[2:])
    yymm = 1 <= s2 <= 12
    mmyy = 1 <= s1 <= 12
    if yymm and mmyy:
        print("AMBIGUOUS")
    elif yymm:
        print("YYMM")
    elif mmyy:
        print("MMYY")
    else:
        print("NA")

if __name__ == "__main__":
    main()