def main():
    a=input()
    b=input()
    for _ in range(len(a)+1):
        if a == b:
            print("Yes")
            break
        a = a[-1] + a[:-1]
    else:
        print("No")
    
if __name__ == "__main__":
    main()