num = int(input())

def digitSum(n):
    s = 0
    while n!=0:
        s += n%10
        n //=10
    return s


arr = []
rev_arr = []
for n in range(1,num):
    arr.append(n)
rev_arr = arr[::-1]

final_arr = []
for n in range(num-1):
    val = digitSum(arr[n]) + digitSum(rev_arr[n])
    final_arr.append(val)

print(min(final_arr))