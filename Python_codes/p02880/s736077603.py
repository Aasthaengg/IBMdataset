def abc144b():
    n = int(input())

    start = 1
    end = 9
    ans = 'No'

    # シンプルな全探索
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if n == i * j:
                ans = 'Yes'
                break
    print(ans)


if __name__ == '__main__':
    abc144b()