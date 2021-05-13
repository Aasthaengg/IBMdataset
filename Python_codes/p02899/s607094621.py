def abc142c_go_to_school():
    n = int(input())
    a = list(zip(range(1, n+1),list(map(int, input().split()))))
    a.sort(key=lambda x: x[1])
    for item in a:
        print(item[0], end=' ')

abc142c_go_to_school()