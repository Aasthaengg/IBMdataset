n = input()
a = input()
a = list(map(int, a.split()))
i = 0
cont_flg = True
while cont_flg:
  if sum(list(map(lambda x: x % 2, a))) == 0:
  	i += 1
  	a = list(map(lambda x: x / 2, a))
  else:
    cont_flg = False
print(i)