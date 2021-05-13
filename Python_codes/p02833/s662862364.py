n = int(input())
if n%2 == 1:
    print(0)
    
else:
    if n < 10:
        print(0)
    else:
        list5 = []
        flag = True
        num = 5
        while flag:
            tmp = n//(num*2)
            if tmp > 0:
                list5.append(tmp)
                num *= 5
            else:
                flag = False
        ans_list = []
        for i in range(len(list5)-1):
            ans_list.append(list5[i] - list5[i+1])
        ans_list.append(list5[-1])
        ans = 0
        for i in range(len(ans_list)):
            ans += ans_list[i]*(i+1)
        print(ans)