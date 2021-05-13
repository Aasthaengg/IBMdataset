N, K = map(int, input().split())
S = input()

zero_index_left = []
flag = False
for i in range(N):
    if flag is False and S[i] == "0":
        zero_index_left.append(i)
        flag = True
    elif S[i] == "1":
        flag = False

if K >= len(zero_index_left):
    print(N)
    exit()
    
zero_index_right = []
S = S[:: -1]
flag = False
for i in range(N):
    if flag is False and S[i] == "0":
        zero_index_right.append(i)
        flag = True
    elif S[i] == "1":
        flag = False
        
ans = 0
for i in range(len(zero_index_left) - K):
    if i == 0:
        ans = max(ans, zero_index_left[i + K])
        ans = max(ans, zero_index_right[i + K])
    else:
        ans = max(ans, zero_index_left[i + K] - N + 1 + zero_index_right[-i] - 1)
        ans = max(ans, zero_index_right[i + K] - N + 1 + zero_index_left[-i] - 1)
print(ans)