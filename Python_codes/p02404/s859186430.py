while (True):
    s = list(map(int, input().strip().split(' ')))

    if s[0] == 0 and s[1] == 0:
        break
    else:
        for i in range(s[0]):
            for j in range(s[1]):
                if i == 0 or i == s[0] - 1:
                    print("#", end="")
                elif j == 0 or j == s[1] - 1:
                    print("#", end="")
                else:
                    print(".",end="")
            print()
    print()
