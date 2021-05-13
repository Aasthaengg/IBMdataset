def solve():
    n = int(input())
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999]
    for i in range(len(x)):
        if n <= x[i]:
            print(x[i])
            exit()



if __name__ == '__main__':
    solve()
