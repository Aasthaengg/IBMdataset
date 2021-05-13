n = int(input())
a_list = list(map(int,input().split()))

all_p = abs(a_list[0]) + abs(a_list[-1])
p_list = [0]*(n+1)
p_list[0] = abs(a_list[0])
p_list[-1] = abs(a_list[-1])
for i in range(len(a_list)-1):
    all_p += abs(a_list[i] - a_list[i+1])
    p_list[i+1] = abs(a_list[i] - a_list[i+1])
    
a_list.insert(0 , 0)
a_list.append(0)
for i in range(len(a_list)-2):
    print(all_p - p_list[i] -p_list[i+1] + abs(a_list[i] - a_list[i+2]))