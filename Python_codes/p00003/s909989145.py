for i in range(int(input())):
    line = sorted(list(map(int, input().split())),reverse=True)
    print('YES' if line[0]**2==line[1]**2+line[2]**2 else 'NO')