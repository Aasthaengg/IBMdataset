n = int(input())
num_list = list(map(int, input().split()))
ans = 1
cnt_list = [0] * n
a = int()

for i in range(1,n):
    if num_list[i-1] > num_list[i]:
        cnt_list[i] = -1
    if num_list[i-1] < num_list[i]:
        cnt_list[i] = 1

while 1 in cnt_list and -1 in cnt_list:
    del cnt_list[:max(cnt_list.index(1),cnt_list.index(-1))]
    cnt_list[0] = 0
    ans += 1

print(ans)