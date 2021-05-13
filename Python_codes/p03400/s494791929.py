N = int(input())
D, X = map(int, input().split())
A_list = [int(input()) for _ in range(N)]

count_chocolate_list = []

for i in range(N):
    k = 0
    chocolate_day_list = []

    while (k*A_list[i] + 1 <= D):
        chocolate_day_list.append(k*A_list[i] + 1)
        chocolate_count = len(chocolate_day_list)
        k += 1
        
    count_chocolate_list.append(chocolate_count)
        
    i += 1
    
ans = sum(count_chocolate_list) + X

print(ans)