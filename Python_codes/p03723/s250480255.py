abc = list(map(int, input().split()))
ans = 0
for i in range(10 ** 6):   
    if abc[0] % 2 != 0:
        print(ans)
        quit()
        break
    else:
        tmp1 = abc[1] // 2 + abc[2] // 2

    if abc[1] % 2 != 0:
        print(ans)
        quit()
        break
    else:
        tmp2 = abc[0] // 2 + abc[2] // 2
        
    if abc[2] % 2 != 0:
        print(ans)
        quit()
        break
    else:
        tmp3 = abc[0] // 2 + abc[2] // 2
        
    abc[0] = tmp1
    abc[1] = tmp2
    abc[2] = tmp3
    ans += 1

print(-1)