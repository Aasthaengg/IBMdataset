n,c,k = map(int,input().split())
list = [int(input()) for _ in range(n)]
sorted_list = sorted(list)
bus = 1
customer = 1
max_hour = sorted_list[0]+k
for i in sorted_list[1:]:
  if i > max_hour or customer >= c:
    bus+=1
    customer=1
    max_hour = i+k
  else:
    customer += 1
print(bus)