L,R = [int(_) for _ in input().split()]
if L//2019 != R//2019:
    mod_min=0
else:
    mod_list=[]

    mod_min = 10**10
    for i in range(L,R):
        for j in range(i+1,R+1):
            if mod_min >= i*j%2019:
                mod_min = i*j%2019
                
            if mod_min == 0:
                break
        if mod_min == 0:
                break
#                 print(i,j,mod_min)
print(mod_min)