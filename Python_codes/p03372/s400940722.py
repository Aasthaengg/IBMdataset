def main():
    import sys
    input = sys.stdin.readline
    N, C = map(int, input().split())

    left = []
    right = []
    left_append = left.append
    right_append = right.append
    for _ in range(N):
        x, v = map(int, input().split())
        left_append([x, v])
        right_append([C - x, v])

    tmp1 = max(0, left[0][1] - left[0][0])
    left_value = [0, tmp1]
    tmp2 = max(0, left[0][1] - 2 * left[0][0])
    left_value_back = [0, tmp2]
    left_value_append = left_value.append
    left_value_back_append = left_value_back.append
    for i in range(1, N):
        left[i][1] += left[i - 1][1]
        tmp1 = max(tmp1 ,left[i][1] - left[i][0])
        left_value_append(tmp1)
        tmp2 = max(tmp2 ,left[i][1] - 2 * left[i][0])
        left_value_back_append(tmp2)

    tmp1 = max(0, right[N - 1][1] - right[N - 1][0])
    right_value = [0, tmp1]
    tmp2 = max(0, right[N- 1][1] - 2 * right[N - 1][0])
    right_value_bakc = [0, tmp2]
    right_value_append = right_value.append
    right_value_bakc_append = right_value_bakc.append
    for i in range(N- 2, -1, -1):
        right[i][1] += right[i + 1][1]
        tmp1 = max(tmp1, right[i][1] - right[i][0])
        right_value_append(tmp1)
        tmp2 = max(tmp2, right[i][1] - 2 * right[i][0])
        right_value_bakc_append(tmp2)

    # print (left)
    # print (left_value)
    # print (left_value_back)
    # print ()
    # print (right)
    # print (right_value)
    # print (right_value_bakc)

    ans = 0
    for i in range(N + 1):
        tmp = max(left_value[i], right_value[N - i])
        tmp = max(tmp, left_value_back[i] + right_value[N - i], left_value[i] + right_value_bakc[N - i])
        ans = max(ans, tmp)

    print (ans)

if __name__ == '__main__':
    main()