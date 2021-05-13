n = int(input())
ans = 0
for a in range(1, n+1):
    t_ans = 0
    for i in range(1, a+1, 2):
        if a%i == 0:
            t_ans +=1
    if t_ans == 8:
        ans +=1
print(ans)