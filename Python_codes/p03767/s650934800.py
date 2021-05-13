n=int(input())
a_list=[int(i) for i in input().split()]
a_list.sort(reverse=True)
second_list=a_list[1:2*n:2]
print(sum(second_list))
