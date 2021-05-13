p = [1, 2, 3, float("inf")]
sum_p = [0, 0, 0, 0] 
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
for i in range(n):
    
    diff = abs(x[i] - y[i])
    if sum_p[3] < diff:
        sum_p[3] = diff  
    sum_p[0] += diff ** p[0]
    sum_p[1] += diff ** p[1]
    sum_p[2] += diff ** p[2]

for i in range(len(sum_p)):
    if i < 3:
        print("{:.8f}".format(sum_p[i] ** (1/p[i])))
    else:
        print("{:.8f}".format(sum_p[i]))

