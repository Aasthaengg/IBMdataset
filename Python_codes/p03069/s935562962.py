N = int(input())
S = input()

left_black = [0] * N
for i in range(N):
    if S[i] == '#':
        left_black[i] += 1
for i in range(N - 1):
    left_black[i+1] = left_black[i] + left_black[i+1]
left_black.insert(0, 0)
# print(left_black)

right_white = [0] * N
for i in range(N):
    if S[i] == '.':
        right_white[i] += 1
for i in range(N-1, 0, -1):
    right_white[i - 1] = right_white[i - 1] + right_white[i]
right_white.append(0)
# print(right_white)

m = 10 ** 6
for i in range(N):
    # if S[i] == '#':
    temp = left_black[i] + right_white[i + 1]
    # print(temp)
    m = min(m, temp)
print(m)

