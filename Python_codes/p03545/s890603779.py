s = input()


for i in range(1 << 3):
    count = int(s[0])
    for j in range(1, 4):
        if i & (1 << j-1):
            count+=int(s[j])
        else:
            count-=int(s[j])
    
    if count == 7:
        ans = s[0] 
        for j in range(1, 4):
            if i & (1 << j-1):
                ans += '+'+s[j]
            else:
                ans += '-'+s[j]

        ans += '=7'
        print(ans)
        exit()