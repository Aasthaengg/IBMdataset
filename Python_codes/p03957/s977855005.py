def main():
    s = list(input())
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]=="C" and s[j]=="F":
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()