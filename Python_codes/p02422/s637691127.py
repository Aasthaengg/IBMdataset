word = input()
q = int(input())

for _ in range(q):
    od = list(map(str, input().split()))

    if od[0] == "print":
        print(word[int(od[1]): int(od[2]) + 1])

    elif od[0] == "reverse":
        if int(od[1]) == 0:
            word = "{}{}{}".format(word[: int(od[1])], word[int(
                od[2])::-1], word[int(od[2]) + 1:])
        else:
            word = "{}{}{}".format(word[: int(od[1])], word[int(
                od[2]): int(od[1]) - 1:-1], word[int(od[2]) + 1:])

    elif od[0] == "replace":
        word = "{}{}{}".format(
            word[: int(od[1])], od[3], word[int(od[2]) + 1:])

