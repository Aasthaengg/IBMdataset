s = input()

a_index = s.find('A')
z_index = s.rfind('Z')
new_s = s[a_index:z_index+1]
print(len(new_s))