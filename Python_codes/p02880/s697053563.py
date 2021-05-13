def abc144b():
    n = int(input())

    start = 1
    end = 9
    flag = False

    # シンプルな全探索
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if n == i * j:
                flag = True
                break

    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    abc144b()