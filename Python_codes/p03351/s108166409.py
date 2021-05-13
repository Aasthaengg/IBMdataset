def main():
    a, b, c, d = map(int, input().split())
    distance = [a, b, c]
    a_c_distance = [a, c]
    a_c_distance.sort()
    if a_c_distance[1] - a_c_distance[0] <= d:
        print('Yes')
        return
    distance.sort()
    if distance[2] - distance[1] <= d and distance[1] - distance[0] <= d:
        print('Yes')
    else:
        print('No')
    
main()