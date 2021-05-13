a, b = tuple(input().split())


def judge():
    def sub_judge1():
        if a == 'H':
            return True
        else:
            return False
    def sub_judge2():
        if b == 'H':
            return True
        else:
            return False

    if sub_judge2():
        return sub_judge1()
    else:
        return not sub_judge1()


if judge():
    print('H')
else:
    print('D')
