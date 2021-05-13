n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_arr = [0] * n
a_arr[0] = a[0]
b_arr = [0] * m
b_arr[0] = b[0]

# Aの上からi冊読むのに何分かかるか
for i in range(1,n):
    a_arr[i] = a_arr[i-1] + a[i]

# Bの上からi冊読むのに何分かかるか
for i in range(1,m):
    b_arr[i] = b_arr[i-1] + b[i]

a_arr.insert(0, 0)
b_arr.insert(0, 0)

# Aから取る上限を探索
i_a_max = 0
for i in range(n+1):
    if a_arr[i] > k:
        break
    else:
        i_a_max = i

# Aから1冊も取らない場合のBの冊数を探索
i_b = 0
for i in range(m+1):
    if b_arr[i] <= k:
        i_b = i
    else:
        break


score = []
# Aをi冊読んだときで全探索
for i_a in range(i_a_max + 1):
    while(True):
        if a_arr[i_a] + b_arr[i_b] <= k:
            break
        elif i_b == 0:
            break
        else:
            i_b -= 1
    score.append(i_a + i_b)
    #print(i_a,i_b)
#print(i_a_max)
print(max(score))