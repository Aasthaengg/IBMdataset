
def main():
    a,b = input().split()
    ab = a+b;
    ab = int(ab)
    for i in range(1,317):
        if i * i == ab:
            print("Yes")
            return 0
    print("No")
    return 0

if __name__ == "__main__":
    main()