n = int(input())
seat_list = [list(map(int,input().split())) for nesya in range(n)]
c = 0
for hoge in seat_list:
  c += (hoge[1]-hoge[0]+1)
print(c)