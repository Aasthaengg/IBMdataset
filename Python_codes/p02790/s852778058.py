
def main():
    a, b = map(int, input().split(" "))
    for i in range(max(a,b)):
        print(min(a,b),end = "")
    print()
    

if __name__ == "__main__":
    main()