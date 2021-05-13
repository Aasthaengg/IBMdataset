N = int(input())
string_list=[int(input()) for i in range(N)]

#print(N,string_list)
nums_unique = list(set(string_list))
print(len(nums_unique))