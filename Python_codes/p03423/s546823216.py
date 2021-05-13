N_str = input()
N = int(N_str)

Gr_num = 3 #○人ずつのグループを作りたい

N_div = N // Gr_num

if N >= 3:
    print(N_div)
elif N < 3:
    print(0)