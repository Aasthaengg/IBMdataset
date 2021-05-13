S = input()

count_0 = 0
count_1 = 0
for s in S:
    if s == "0":
        count_0 += 1
    else:
        count_1 += 1
        
print(2 * min(count_0, count_1))