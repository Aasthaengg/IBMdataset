def slove(n, m):
    if n < m:
        tmp = "<"
    elif n > m:
        tmp = ">"
    else:
        tmp = "="
    return tmp

if __name__ == "__main__":
    n, m = [i for i in input().split()]
    print(slove(n, m))