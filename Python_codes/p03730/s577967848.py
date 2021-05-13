a, b, c = map(int, input().split())

tmp_list = []
i = 1
while True:
    tmp = a * i % b
    if tmp == c:
        print("YES")
        exit()
    else:
        if tmp in tmp_list:
            print("NO")
            exit()
        tmp_list.append(tmp)
        i += 1
