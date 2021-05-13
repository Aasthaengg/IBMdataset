s = list(str(input()))
s_a = [i for i, x in enumerate(s) if x == 'A']
a = min(s_a)
s_z = [i for i, x in enumerate(s) if x == 'Z']
z = max(s_z)
print(z-a+1)