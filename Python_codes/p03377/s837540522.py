A, B, X = map(int, input().split())

def main():
    if A + B < X or A > X:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
