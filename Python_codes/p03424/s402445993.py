N = int(input())
S_i_list = input().split()
if len(set(S_i_list)) == 3:
    print('Three')
else:
    print('Four')