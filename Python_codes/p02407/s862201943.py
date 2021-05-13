number_list=[]
for i in range(2):
    a=input().split()
    number_list.append(a)
for n in range(int(number_list[0][0])):
    if n!=int(number_list[0][0])-1:
        print('{0} '.format(number_list[1][int(number_list[0][0])-1-n]), end='')
    else:
        print('{0}'.format(number_list[1][int(number_list[0][0])-1-n]))