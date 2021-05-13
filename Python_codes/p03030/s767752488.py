lst = []
for i in range(int(input())):
    S,P = input().split()
    lst.append([S,int(P),i])

sorted_point = sorted(lst,key = lambda x: x[1], reverse = True)
sorted_name = sorted(sorted_point,key = lambda x: x[0], reverse = False) 

for i in sorted_name:
    print(i[2] + 1)