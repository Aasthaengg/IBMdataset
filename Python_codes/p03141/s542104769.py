n = int(input())
li = []
for i in range(n):
    a,b = map(int,input().split())
    tmp = [a+b,a,b]
    li.append(tmp)
li.sort(reverse=True)
x_sum = 0
y_sum = 0
for i,l in enumerate(li):
    if i%2 == 0:
        x_sum += l[1]
    else:
        y_sum += l[2]
print(x_sum-y_sum)
#print(li)