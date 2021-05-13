n = int(input())
a = input().split()
for i in range(len(a)):
    a[i]=int(a[i])
# print(a)
a.sort()
# print(a)
# #両端をとっておく
hashi1 = a[0]
hashi2 = a[-1]
a.remove(a[0])
a.remove(a[-1])
# print(a)
minus_list = []
plus_list = []
printlist = []
for i in range(len(a)):
    if a[i]>0:
        plus_list.append(a[i])
    else:
        minus_list.append(a[i])
# print(minus_list)
# print(plus_list)
for j in range(len(minus_list)):
    printlist.append(hashi2)
    printlist.append(minus_list[j])
    hashi2 = hashi2-minus_list[j]
    
for l in range(len(plus_list)):
    printlist.append(hashi1)
    printlist.append(plus_list[l])
    hashi1 = hashi1 - plus_list[l]
    
printlist.append(hashi2)
printlist.append(hashi1)
print(hashi2-hashi1)
# print(printlist)
for n in range(0,len(printlist),2):
    print(printlist[n],printlist[n+1])