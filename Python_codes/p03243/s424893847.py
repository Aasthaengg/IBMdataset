def main():
    s=int(input())
    for n in range(s, 1000):
        ns=str(n)
        if ns[0] == ns[1] == ns[2]:
            print(ns)
            return

if __name__ == "__main__":
    main()