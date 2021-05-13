def resolve():
    n, k = map(int, input().split())
    input_list = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        input_list.append([ai, bi])

    input_list.sort()
    count_dic = {}
    prev_max = 0
    for key, value in input_list:
        if key in count_dic.keys():
            count_dic[key] += value
        else:
            count_dic[key] = value + prev_max
        prev_max = count_dic[key]

        if count_dic[key] >= k:
            print(key)
            return
          
resolve()