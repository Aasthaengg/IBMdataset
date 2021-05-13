s = input()
s_list = list(s)
l = len(s_list)
k = []

for i in range(0,l,2):
    k.append(s_list[i])

s_joined = ''.join(k)

print("{}".format(s_joined))