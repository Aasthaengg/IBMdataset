N,x = list(map(int,input().split()))
a =  list(map(int,input().split()))
counter = 0
for i in range(N-1):
    sum_a = a[i] + a[i+1] 
    if sum_a > x:
        if sum_a - x > a[i+1]:
            counter += sum_a -x
            a[i] = a[i] -(sum_a-x-a[i+1]) #この行はなくてもいい
            a[i+1] = 0
        else:
            counter += sum_a-x
            a[i+1] = a[i+1] - (sum_a -x)
print(counter)
