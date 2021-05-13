n = int(input())
list_l = [int(x) for x in input().split()]

count = 0

# 組合せnCpの総当たりforループ（計算速度遅）
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if list_l[i] != list_l[j] != list_l[k] and list_l[i] != list_l[k]:
                if list_l[i] < list_l[j] + list_l[k] and list_l[j] < list_l[i] + list_l[k] and list_l[k] < list_l[i] + list_l[j]:
                    
                    count += 1
print(count)