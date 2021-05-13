N = int(input())
A_array = list(map(int, input().split()))

ans = 0

sum_dic = {}

for i in range(N-1):
    s = i + A_array[i]
    if s in sum_dic:
        sum_dic[s] += 1
    else:
        sum_dic[s] = 1
    t = A_array[i+1] - (i+1)
    if -t in sum_dic:
        ans += sum_dic[-t]


print(ans)