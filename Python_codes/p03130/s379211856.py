def main():
    a = [0]*4
    for _ in range(3):
        x, y = map(int, input().split())
        a[x-1] += 1
        a[y-1] += 1
    a.sort()
    if a[0] == 1 and a[1] == 1 and a[2] == 2 and a[3] == 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()