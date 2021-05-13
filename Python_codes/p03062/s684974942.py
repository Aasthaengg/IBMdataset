N = int(input())

array = [int(i) for i in input().split()]
calc_array = []

cnt = 0

for n in array:
    if n < 0:
        cnt += 1
    calc_array.append(abs(n))
        
if cnt % 2 == 0 or 0 in calc_array:
    output = sum(calc_array)
else :
    output = sum(calc_array) - (2*min(calc_array))
    
print(output)