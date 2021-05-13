if __name__ == '__main__':
    x = list(input())
    sl = []
    ans = 0
    for i in x:
        if i == "S":
            sl.append(1)
        else:
            if len(sl) != 0:
                ans += sl.pop()

    print(len(x) - ans * 2)
