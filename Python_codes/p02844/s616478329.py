n = int(input())
num = input()
 
password_list = []
initial_list = []
initial_list2 = []
initial_list3 = []
 
for i in range(len(num)-2):
    initial_list2 = []
    if num[i] in initial_list:
        continue
    elif len(initial_list) == 10:
        break
    else:
        initial_list.append(num[i])
        for j in range(i+1,len(num)-1):
            initial_list3 = []
            if num[j] in initial_list2:
                continue
            elif len(initial_list2) == 10:
                break
            else:
                initial_list2.append(num[j])
                for k in range(j+1,len(num)):
                    if num[k] in initial_list3:
                        continue
                    elif len(initial_list3) == 10:
                        break
                    else:
                        initial_list3.append(num[k])
                        target = num[i] + num[j] + num[k]
                        if target not in password_list:
                            password_list.append(target)
                            
print(len(password_list))