N = input()
str=''
str_list=list(N)
str_list2= list(reversed(N))
if str.join(str_list)==str.join(str_list2):
    print('Yes')
else:
    print('No')
