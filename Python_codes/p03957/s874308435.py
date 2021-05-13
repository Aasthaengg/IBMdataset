def main():

    s = input()
    Cidx = -1
    for i in range(len(s)):
        if s[i] == "C":
            Cidx = i
            break
    if Cidx == -1:
        return "No"

    for i in range(Cidx+1, len(s)):
        if s[i] == "F":
            return "Yes"
    return "No"

if __name__ == '__main__':
    print(main())