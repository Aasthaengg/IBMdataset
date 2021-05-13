
n = int(input())
num_list = [ int(v) for v in input().split() ]

multi_list = [[num_list[0]]]

for i in range(1,n):
    if num_list[i] == multi_list[-1][-1]:
        multi_list[-1].append(num_list[i])
    else:
        multi_list.append([num_list[i]])
    
print(sum(map(lambda x: len(x)//2 ,multi_list)))