S = input()
is_flag = True
if S[2] != S[3]:
    is_flag = False
if S[4] != S[5]:
    is_flag = False
if is_flag == True:
    print("Yes")
elif is_flag == False:
    print("No")