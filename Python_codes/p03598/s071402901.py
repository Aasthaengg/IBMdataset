N = int(input())
K = int(input())
x_list = [int(i) for i in input().split()]

sum = 0
for x in x_list:
  sum += min(x * 2 , abs(K-x) * 2)
  
print(sum)