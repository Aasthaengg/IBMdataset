def main():
    n = int(input())
    inlis = []
    for _ in range(n):
        a = int(input())
        inlis.append(a)
    saidai = max(inlis)
    kosuu = inlis.count(saidai)
    inlis2 = sorted(inlis)
    saidai2 = inlis2[-2]
    for i in range(n):
        if inlis[i] != saidai:
            print(saidai)
        else:
            print(saidai2)

if __name__ == "__main__":
    main()
