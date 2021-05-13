# coding: utf-8
def main():
    N = int(input())
    s = input()
    rcount = 0
    # bcount = 0
    for si in s:
        if si == 'R':
            rcount += 1
        # elif si == 'B':
        #     bcount += 1
    bcount = N - rcount
    if rcount > bcount:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()