if __name__ == '__main__':
    # ??????????????\???
    num = int(input())
    triangles = []
    for i in range(num):
        triangles.append([int(x) for x in input().split(' ')])

    # ??´?§?????§???¢?????????????????????
    results = []
    for t in triangles:
        t.sort()
        if t[0]**2 + t[1]**2 == t[2]**2:
            results.append('YES')
        else:
            results.append('NO')

    # ???????????????
    for r in results:
        print(r)