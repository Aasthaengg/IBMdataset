s=input()

count=0
a_list=[]
b_list=["A", "C", "G", "T"]
num=len(s)

for i in range(num):
    if s[i] in b_list:
        count+=1
    else:
        a_list.append(count)
        count=0
a_list.append(count)

print(max(a_list))