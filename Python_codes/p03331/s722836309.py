
n=int(input())

def digitSum(n):
    s = str(n)
    array = list(map(int, list(s)))
    return sum(array)

min=9999999
#b= n-a
for a in range(1,n):
    b=n-a
    sum_a=digitSum(a)
    sum_b=digitSum(b)
    sum_ab=int(sum_a)+int(sum_b)
   
    if sum_ab < min:
        min=sum_ab

print(min)

