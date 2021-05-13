url = "https://atcoder.jp/contests/abc090/tasks/arc091_a"
import copy
def main():
    tate, yoko = list(map(int, input().split()))
    count = 0
    if tate == 1 and yoko == 1:
        print("1")
        exit()
    elif tate == 1:
        print(yoko - 2)
        exit()
    elif yoko == 1:
        print(tate - 2)
        exit()
    count += (yoko - 2) * (tate - 2)
    print(count)




if __name__ == '__main__':
    main()


