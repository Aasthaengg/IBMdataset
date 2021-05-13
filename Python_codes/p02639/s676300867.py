
def main():
    xls = list(map(int, input().split()))
    i = 1
    for _ in xls:
        if _ == 0:
            break
        else:
            i += 1

    print(i)



main()
