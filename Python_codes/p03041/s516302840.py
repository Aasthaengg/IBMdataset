small = ['a', 'b', 'c']
capital = ['A', 'B', 'C']
 
tmp = input().split(" ")
N = int(tmp[0])
K = int(tmp[1])
str = list(input())
 
str[K - 1] = small[capital.index(str[K - 1])]
 
print("".join(str))