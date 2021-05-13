def main():
    s = input()
    nagasa = len(s)

    for i in range(nagasa):
        if i % 2 == 0 and s[i] == "L":
            print("No")
            exit()
        elif i % 2 != 0 and s[i] == "R":
            print("No")
            exit()
    print("Yes")

    
    
    
if __name__ == "__main__":
    main()
