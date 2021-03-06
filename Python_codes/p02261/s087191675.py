#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C&lang=jp
#??????????????????
#??????????????????????°???????????????£?????´???????????´?????¨??\?????????????????????????????????????????´????????????
#??????????????????????????????????°????????????????????????´???????????????????????????????????????????????¨??????

def bubble_sort(origin_list):
    list_length = len(origin_list)
    target_list = [i for i in origin_list]#??°????????????????????????
    flag = True
    change_count = 0
    top_index = 1
    while flag:
        flag = False
        for i in range(top_index, list_length)[::-1]:
            if target_list[i][1] < target_list[i - 1][1]:
                tmp = target_list[i]
                target_list[i] = target_list[i - 1]
                target_list[i - 1] = tmp
                change_count += 1
                flag = True
        top_index += 1       
    return target_list

def selection_sort(origin_list):
    list_length = len(origin_list)
    target_list = [i for i in origin_list]#??°????????????????????????
    change_count = 0
    for i in range(list_length):
        min_index = i
        for j in range(i, list_length):
            if target_list[j][1] < target_list[min_index][1]:
                min_index = j
        else:
            if not i == min_index:
                tmp = target_list[i]
                target_list[i] = target_list[min_index]
                target_list[min_index] = tmp
                change_count += 1
    return target_list

def check_stable(origin_list, target_list):
    for i, origin_v in enumerate(origin_list):
        for origin_v2 in origin_list[i+1:]:
            if origin_v[1] == origin_v2[1]:
                for j, target_v in enumerate(target_list):
                    for target_v2 in target_list[j+1:]:
                        if origin_v == target_v2 and origin_v2 == target_v:
                            return "Not stable"
    return "Stable"

def stable_sort(target_list):
    print(*bubble_sort(target_list))
    print(check_stable(target_list, bubble_sort(target_list)))
    print(*selection_sort(target_list))
    print(check_stable(target_list, selection_sort(target_list)))
    
def main():
    n_list = int(input())
    target_list = [a for a in input().split()]
    stable_sort(target_list)
    
if __name__ == "__main__":
    main()