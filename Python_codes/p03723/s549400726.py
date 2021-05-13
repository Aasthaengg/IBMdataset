def exchange(l):
    newlist = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            if i != j:
                newlist[i] += l[j]//2
    return newlist


def containsOdd(l):
    for i in range(3):
        if l[i] % 2 == 1:
            return True
    return False


def isAllEquals(l):
    if l[0] == l[1] == l[2]:
        return True
    return False


def main():
    cookies = [int(x) for x in input().split()]
    ans = 0
    while True:
        if isAllEquals(cookies):
            if cookies[1] % 2 == 1:
                print(0)
                return
            print(-1)
            return 0
        if containsOdd(cookies):
            print(ans)
            return 0
        cookies = exchange(cookies)
        ans += 1


if __name__ == '__main__':
    main()
