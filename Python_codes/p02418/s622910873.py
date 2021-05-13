str_in = input()
str_val = input()

for i in range(len(str_in),-1,-1):
    flag = str_val in str_in  # check if input value is in string
    if flag:
        break
    if str_val[:i] == str_in[0-i:] and str_in.find(str_val[i:]) == 0:  #first, check if substring till i-index is found in the last part of string. If yes, check rest of input value is found in the beginning of string
        flag = True
        break

if flag:
    print('Yes')
else:
    print('No')