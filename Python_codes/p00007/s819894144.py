n = input()
ans = 100000

for i in range(int(n)):
    add = int(ans*0.05)
    #print("first_add:" + str(add))
    add_list = list(str(add))
    digits = len(add_list)    
    sub3 = int(add_list[digits-3]+add_list[digits-2]+add_list[digits-1])
    add = int("".join(add_list))
    #print("sub3:"+ str(sub3))
    if sub3<1000 and sub3 > 0:
        add = add - sub3 + 1000
        #print("revised_add:" + str(add))
        
    ans = ans + add
    #print("ans:" + str(ans))

print(ans)