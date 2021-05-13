
def sign(x):
    return (x > 0) - (x < 0)


def main():
    _ = int(input())
    a = map(int, input().split())
    ans = []
    arr = []
    state = 0
    for an in a:
        if len(arr) < 2:
            arr.append(an)
        else:
            state += (arr[-1] - arr[-2])
            if state == 0:
                arr.append(an)
            else:
                current = an - arr[-1]
                if current == 0 or sign(state) == sign(current):
                    arr.append(an)
                else:
                    ans.append(arr)
                    arr = [an]
                    state = 0
    ans.append(arr)

    print(len(ans))


if __name__ == '__main__':
    main()
