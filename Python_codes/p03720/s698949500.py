n,m = map(int,input().split())
count_list = [0] * n

list = [input() for i in range(m)]

for i in range(m):
    ary = list[i].split()
    count_list[int(ary[0])-1] += 1
    count_list[int(ary[1])-1] += 1

for i in range(n):
  print(count_list[i])