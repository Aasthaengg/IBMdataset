s = input()
a_list = [i for i, x in enumerate(s) if x == 'A']
z_list = [i for i, x in enumerate(s) if x == 'Z']
a = a_list[0]
z = z_list[-1]
print(len(s[a:z+1]))