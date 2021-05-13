N = int(input())
S = input()

ans = 0
for i in range(1000):
    judge = False
    p = 0
    if i >= 0 and i < 10:
        number = "00" + str(i)
    elif i >= 10 and i < 100:
        number = '0' + str(i)
    else:
        number = str(i)
    
    for j in range(N):
        if number[p] == S[j]:
            p += 1
            if p == 3:
                ans += 1
                break
            

print(ans)