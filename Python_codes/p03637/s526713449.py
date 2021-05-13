
url = "https://atcoder.jp//contests/abc069/tasks/arc080_a"

def main():
    s = int(input())
    t = list(map(int, input().split()))
    dic = {1: 0, 2: 0, 4: 0}

    for v in t:
        if v % 4 == 0:
            dic[4] += 1
        elif v % 2 == 0:
            dic[2] += 1
        else:
            dic[1] += 1
    if dic[1] <= dic[4]:
        print('Yes')
    elif dic[1] <= dic[4] + 1:
        if dic[2] != 0:
            print('No')
        else:
            print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
