N = int(input())
arr = list(map(int, input().split()))

dic = {}
j_arr =[]

ans = 0
for i in range(N):
    if i+arr[i] not in dic:
        dic[i+arr[i]] = 0
    dic[i+arr[i]] += 1
    j_arr.append(-1*arr[i]+i)
    if -1*arr[i]+i in dic:
        ans += dic[-1*arr[i]+i]

print(ans)