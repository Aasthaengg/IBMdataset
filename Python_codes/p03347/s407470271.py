n = int(input())
num_list = [ int(input()) for i in range(n) ]
num_list.reverse()


ans = 0
t = 0
for i in range(n):
    t = max(t-1, 0)
    if num_list[i] != 0 and num_list[i] > t:
        ans += num_list[i]
        t = num_list[i]
    elif num_list[i] < t:
        ans = -1
        break

if t != 0:
    ans = -1
print(ans)