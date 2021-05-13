s = input()
k = int(input())

l = len(s)
cnt = 0
cnt_list = [0]

for i in range(l-1):#sの中での連続数
    if s[i] == s[i+1]:
        cnt += 1
        cnt_list.append(cnt)
    else:
        cnt = 0
        cnt_list.append(cnt)
#print(cnt_list)

for i in range(l-1):#sの末尾と最初がつながっているとき
    if s[-1] == s[i]:
        cnt += 1
        cnt_list.append(cnt)
    else:
        break
#print(cnt_list)
L = len(cnt_list)

if len(set(s)) == 1:#1文字のみのとき
    print(l*k//2)
    
elif k == 1:#k = 1の時  
    ans = 0
    for i in cnt_list[:l]:#最初のl文字での回数
        if i % 2 == 1:
            ans += 1
    print(ans)
    
else:
    cnt_ref = cnt_list[L-l:] #繰り返し部分
    ans_ref = 0
    for i in cnt_ref:
        if i % 2 == 1:
            ans_ref += 1
    num_ref = (k*l-L) // l #num回繰り返す 
    #print("ans_ref =" ,ans_ref)
    
    amari = (k*l-L) % l
    ans_amari = 0
    for i in cnt_ref[:amari]:
        if i % 2 == 1:
            ans_amari += 1
    #print("ans_amari", ans_amari)
    #print("cnt_ref[:amari] = ", cnt_ref[:amari])  
    
    ans = 0
    for i in cnt_list:
        if i % 2 == 1:
            ans += 1
    #print("ans = ",ans)
    
    ans += ans_amari + ans_ref * num_ref
    print(ans)