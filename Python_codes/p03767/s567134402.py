N = int(input())
a_list = [int(e) for e in input().split()]
a_list.sort(reverse=True)
a_list = [0] + a_list 
ans_list= list()

for i in range(1,len(a_list)):
    if i%2 == 0:
        ans_list.append(a_list[i])
        if len(ans_list) == N:
            print(sum(ans_list))
            break