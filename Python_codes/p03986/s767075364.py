if __name__ == "__main__":
    x = input()

    count = 0
    ans = len(x)
    for i in range(len(x)):
        if x[i] == 'S':
            count += 1
        elif count > 0 and x[i] == 'T':
            ans -= 2
            count -= 1
        else:
            count = 0

    print(ans)
