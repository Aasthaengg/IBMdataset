s = input()
t = input()

dic = {}
dic2 = {}

for i,j in zip(s,t):
    if j not in dic:
        if i in dic2:
            print("No")
            exit()
        dic[j] = i
        dic2[i] = j
    else:
        if dic[j] != i:
            print("No")
            exit()
print("Yes")