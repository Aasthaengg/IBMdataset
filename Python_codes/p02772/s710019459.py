S_list = [input() for i in range(2)]
S_list_1 = list(map(int,S_list[1].split()))

for i in S_list_1:   
    if i % 2 == 0 :
        if i % 3 !=0 and i % 5 !=0 :
            result="DENIED"
            break
    else:
        result="APPROVED"        
print(result)