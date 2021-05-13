def main():
    s = input()

    na, nb, nc = 0, 0, 0

    for c in s:
        if c == "a":
            na += 1

        if c == "b":
            nb += 1
        
        if c == "c":
            nc += 1

    mi = min(na, nb, nc)

    na -= mi
    nb -= mi
    nc -= mi

    if na >= 2 or nb >= 2 or nc >= 2:
        print("NO")
    else:
        print("YES")
        
if __name__ == "__main__":
    main()