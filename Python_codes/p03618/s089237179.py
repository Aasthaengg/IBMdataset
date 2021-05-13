A = input()
A_dic = {}
for i in A:
    if i in A_dic:
        A_dic[i] += 1
    else:
        A_dic[i] = 1

m = 1
for i in range(2,len(A)+1):
    m += len(A) - i + 1

for i in A_dic.values():
    m -= (i*(i-1))/2

print(int(m))
