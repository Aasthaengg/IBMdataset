def main():
    s=input()
    c,f=False,False
    for i in s:
        if c and i == "F":
            f=True
        elif i == "C":
            c=True
    print("Yes" if c and f else "No")
    
if __name__ == "__main__":
    main()