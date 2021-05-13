def main():
    n = map(int, input().split())
    inlis = list(map(int, input().split()))
    sortlis = sorted(inlis)

    tmp = 0
    for i in range(len(inlis)):
        if inlis[i] != sortlis[i]:
            tmp += 1
    if tmp == 0 or tmp == 2:
        print("YES")
    else:
        print("NO")

    
if __name__ == "__main__":
    main()
