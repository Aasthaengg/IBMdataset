def main():
    s = input()

    bool = False
    l = len(s)

    while bool == False:
        l = l - 2
        if s[0:l//2] == s[(l+1)//2:l]:
            bool = True

    print(l)

        
if __name__ == '__main__':
    main()