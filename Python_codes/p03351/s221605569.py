a_point, b_point, c_point, possible_of_distance = map(int, input().split())

# a地点とb地点の距離
if a_point > b_point:
    a_b_distance = a_point - b_point
elif b_point > a_point:
    a_b_distance = b_point - a_point
elif a_point == b_point:
    a_b_distance = 0

# b地点とc地点の距離
if c_point > b_point:
    b_c_distance = c_point - b_point
elif b_point > c_point:
    b_c_distance = b_point - c_point
elif c_point == b_point:
    b_c_distance = 0

# a地点とc地点の距離
if a_point > c_point:
    a_c_distance = a_point - c_point
elif c_point > a_point:
    a_c_distance = c_point - a_point
elif a_point == c_point:
    a_c_distance = 0


# コンタクト可能かの処理。
if a_c_distance <= possible_of_distance:
    print('Yes')
elif a_c_distance > possible_of_distance:
    if a_b_distance <= possible_of_distance and b_c_distance <= possible_of_distance:
        print('Yes')
    else:
        print('No')
