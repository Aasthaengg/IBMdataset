def func():
    a,b,c = input().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)
    cnt = 0

    for i in range(a,b+1):
        if 0 == c % i:
            cnt = cnt +1

    print(cnt)

    return 0

if __name__ == "__main__":
    ret = func()
