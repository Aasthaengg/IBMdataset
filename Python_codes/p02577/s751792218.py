N = input()
N_list = []
for i in N:
    N_list.append(int(i))

if sum(N_list) % 9 == 0:
    print("Yes")
else: print("No")