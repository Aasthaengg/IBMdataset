n = int(input())
list = list(map(int, input().split()))
sorted_list = sorted(list, reverse=True)
sum = 0
for i in range(n):
  sum += sorted_list[2*i+1]
print(sum)