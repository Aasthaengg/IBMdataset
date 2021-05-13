def main():
    a,b,c,d=map(int,input().split())
    print("Yes" if (abs(c-b) <= d and abs(b-a) <= d) or abs(c-a) <= d else "No")

if __name__ == "__main__":
    main()