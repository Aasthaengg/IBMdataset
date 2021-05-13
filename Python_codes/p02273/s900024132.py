#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_C&lang=jp
import math
def get_koch_curve_points(curve_num, points):

    result = points
    for i in range(curve_num):
        next_list = []
        for j in range(len(result) - 1):
            next_list.append(result[j])
            next_list.extend(koch_curve(result[j], result[j + 1]))
        next_list.append(result[-1])
        result = next_list
        
    return result

def koch_curve(left_points, right_points):
    len_x = right_points[0] - left_points[0]
    len_y = right_points[1] - left_points[1]

    distance_x = len_x / 3
    distance_y = len_y / 3

    s = (left_points[0] + distance_x, left_points[1] + distance_y)
    t = (right_points[0] - distance_x, right_points[1] - distance_y)

    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))
    u = (s[0] + distance_x * cos60 - distance_y * sin60, s[1] + distance_x * sin60 + distance_y * cos60)
    return [s, u, t]

if __name__ == "__main__":

    curve_num = int(input())
    res = get_koch_curve_points(curve_num, [(0,0),(100,0)])
    print("\n".join([str(x) + " " + str(y) for x,y in res]))