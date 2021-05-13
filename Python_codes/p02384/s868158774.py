#アルゴリズム関数-サイコロを回転させる
def dice_rotation(list1, str1):
    if str1 == "S":
        list1[0],list1[1],list1[4],list1[5] = list1[4],list1[0],list1[5],list1[1]
    elif str1 == "E":
        list1[0],list1[2],list1[3],list1[5] = list1[3],list1[0],list1[5],list1[2]
    elif str1 == "N":
        list1[0],list1[1],list1[4],list1[5] = list1[1],list1[5],list1[0],list1[4]
    elif str1 == "W":
        list1[0],list1[2],list1[3],list1[5] = list1[2],list1[5],list1[0],list1[3]
    return list1

#アルゴリズム関数-上面・前面の番号を指定番号へサイコロを回転させる
def dice_find(list1, int1, int2):
    position_numnber = list1.index(int2)
    if position_numnber == 0:
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 2:
        list1 = dice_rotation(list1, "W")
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 3:
        list1 = dice_rotation(list1, "E")
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 4:
        list1 = dice_rotation(list1, "S")
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 5:
        list1 = dice_rotation(list1, "N")
    position_numnber = list1.index(int1)
    if position_numnber == 2:
        list1 = dice_rotation(list1, "W")
    elif position_numnber == 3:
        list1 = dice_rotation(list1, "E")
    elif position_numnber == 5:
        list1 = dice_rotation(list1, "W")
        list1 = dice_rotation(list1, "W")
    return list1

#インプットdataの格納
input_number = list(map(int, input().split()))
input_count = int(input())
result = list()

#処理の実行
for count in range(input_count):
    check_number = list(map(int, input().split()))
    input_number = dice_find(input_number, check_number[0], check_number[1])
    result.append(input_number[2])

#結果表示
[print(i) for i in result] 

