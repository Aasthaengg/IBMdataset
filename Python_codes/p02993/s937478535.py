def main():
    s = input()
    f = True
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            f = False
    if f:
        print("Good")
    else:
        print("Bad")

if __name__ == "__main__":
    main()