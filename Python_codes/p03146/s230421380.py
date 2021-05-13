N = int(input())

d = {N}
temp = N
for i in range(2, 10**7):
    if temp%2 == 0:
        temp //= 2
    else:
        temp = 3*temp + 1
    if {temp} & d:
        print(i)
        break
    else:
        d.add(temp)