def run():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    for d in data:
        _data = d[:]
        mx = max(_data)
        _data.remove(mx)
        if mx**2 == sum([x**2 for x in _data]):
            print('YES')
        else:
            print('NO')
        

if __name__ == '__main__':
    run()


