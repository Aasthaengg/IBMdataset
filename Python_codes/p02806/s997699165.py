n = int(input())
st = list([input().split() for _ in range(n)])
x = input()

time = 0
flag = False
for i in st:
  if flag:
    time += int(i[1])
  if i[0]==x:
    flag = True
print(time)