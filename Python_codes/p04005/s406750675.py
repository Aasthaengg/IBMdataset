A,B,C = map(int,input().split(' '))
num_list = [A,B,C]
list_s = sorted(num_list)
if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
    print(list_s[0]*list_s[1])
else:
    print(0)