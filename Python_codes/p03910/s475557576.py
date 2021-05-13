n = int(input())
tmp = 0
li = []
for i in range(n):
    if i*(i+1)/2 >= n:
        tmp = i
        break
new_li = [x for x in range(1,tmp+1)]
#print(new_li)
if sum(new_li) - n > 0:
    new_li.remove(sum(new_li) - n)
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for n in new_li:
        print(n)