n = int(input())
hn = [int(num) for num in input().split()]

max_num = 0
for i in range(n):
    if hn[i] < max_num - 1  :
        print("No")
        exit()
    max_num = max(max_num, hn[i])
print("Yes")