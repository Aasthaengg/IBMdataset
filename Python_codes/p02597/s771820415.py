def main():
    n = int(input())
    s = input()
    rcount = s.count('R')
    diff = s[0:rcount].count("W")

    print(diff)




if __name__ == "__main__":
    main()