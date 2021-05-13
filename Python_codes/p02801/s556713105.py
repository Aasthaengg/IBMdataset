import string

C = input()

a_z = string.ascii_lowercase
print(a_z[a_z.index(C) + 1])