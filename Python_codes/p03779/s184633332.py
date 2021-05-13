def main():
    X = int(input())
    for t in range(pow(10, 6)):
        s = (t*(t+1))//2
        if s >= X:
            print(t)
            break

if __name__ == "__main__":
    main()
