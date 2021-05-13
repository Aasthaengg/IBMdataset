a_point, b_point, c_point, possible_of_distance = map(int, input().split())

a_b_distance = abs(a_point - b_point)
a_c_distance = abs(a_point - c_point)
b_c_distance = abs(b_point - c_point)

if a_c_distance <= possible_of_distance:
    print('Yes')
elif max(a_b_distance, b_c_distance) <= possible_of_distance:
    print('Yes')
elif a_c_distance == 0:
    print('Yes')
else:
    print('No')