n,k=[int(i) for i in input().split()]
l_list=[int(i) for i in input().split()]

l_list.sort(reverse=True)

new_list=l_list[:k]
print(sum(new_list))