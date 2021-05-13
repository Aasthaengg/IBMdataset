dish = [int(input()) for i in range(5)]
a = [i%10 for i in dish]

x=10
for i in a:
  if i>0:
    x=min(x,i)
if x ==10:
  x = 0
y = a.index(x)
l = dish.pop(y)

time = [(i//10+1)*10  if i%10 != 0 else i for i in dish]

ans = sum(time) + l
print(ans)