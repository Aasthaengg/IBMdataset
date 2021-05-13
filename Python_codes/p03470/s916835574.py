#listが要素に持つ配列について、target_indexのインデックスの要素の出現回数をディクショナリに出力
def count(list, target_index = None):
    dict = {}
    if target_index == None:
        for i in range(len(list)):
            dict[list[i]] = dict.get(list[i], 0) + 1
    if target_index != None:
        for i in range(len(list)):
            dict[list[i][target_index]] = dict.get(list[i][target_index], 0) + 1
    return dict

#n回の整数入力を受け付け
def input_int_list(n):
    list = [0]*n
    for i in range(n):
        list[i] = int(input())
    return list

num = int(input())
discs = input_int_list(num)

print(str(len(count(discs))))
