
def main():
    n, k = map(int, input().split(" "))
    s =set()
    for i in range(k):
        _ = input()
        a = list(map(int, input().split(" ")))
        for j in range(len(a)):
            s.add(a[j])
    print(n - len(s))

if __name__ == "__main__":
    main()