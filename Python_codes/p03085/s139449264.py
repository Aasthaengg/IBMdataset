def main():
    b = input()
    for i in range(len(b)):
        if b[i] == "A":
            print("T",end="")
        elif b[i] == "T":
            print("A",end="")
        elif b[i] == "C":
            print("G",end="")
        elif b[i] == "G":
            print("C",end="")
    print()
if __name__ == "__main__":
    main()