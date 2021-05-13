n = int(input())


ans_num = 0
for i in range(1, n+1):

    if i % 2 != 0:
        ans = 0        
        for j in range(1, i+1):
            if i % j ==0:
                ans += 1
        if ans == 8:
            ans_num += 1

print(ans_num)