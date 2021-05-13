n_str = input()
a_str, b_str = n_str.split()
a = int(a_str)
b = int(b_str)

if a <= 8:
    if b <= 8:
        print('Yay!')
    else:
        print(':(')
elif a > 8:
    print(':(')