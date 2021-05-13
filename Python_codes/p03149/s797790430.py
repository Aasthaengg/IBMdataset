def main():
    a = [0]*10
    b = list(map(int, input().split()))
    for v in b:
        a[v] += 1
    if a[1] == 1 and a[9] == 1 and a[7] == 1 and a[4] == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()