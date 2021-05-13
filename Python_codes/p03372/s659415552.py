N, C = map(int, input().split())

left = []
right = []
for _ in range(N):
    x, v = map(int, input().split())
    left.append([x, v])
    right.append([C - x, v])

tmp1 = max(0, left[0][1] - left[0][0])
left_value = [0, tmp1]
tmp2 = max(0, left[0][1] - 2 * left[0][0])
left_value_back = [0, tmp2]
for i in range(1, N):
    left[i][1] += left[i - 1][1]
    tmp1 = max(tmp1 ,left[i][1] - left[i][0])
    left_value.append(tmp1)
    tmp2 = max(tmp2 ,left[i][1] - 2 * left[i][0])
    left_value_back.append(tmp2)

tmp1 = max(0, right[N - 1][1] - right[N - 1][0])
right_value = [0, tmp1]
tmp2 = max(0, right[N- 1][1] - 2 * right[N - 1][0])
right_value_bakc = [0, tmp2]
for i in range(N- 2, -1, -1):
    right[i][1] += right[i + 1][1]
    tmp1 = max(tmp1, right[i][1] - right[i][0])
    right_value.append(tmp1)
    tmp2 = max(tmp2, right[i][1] - 2 * right[i][0])
    right_value_bakc.append(tmp2)

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