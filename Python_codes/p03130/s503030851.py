dict = {"1":0, "2":0, "3":0, "4":0}
for i in range(3):
    a, b = input().split()
    dict[a] += 1
    dict[b] += 1

cnt = 0    
for value in dict.values():
    if(value >= 2):
        cnt += 1
print("YES" if cnt >= 2 else "NO")