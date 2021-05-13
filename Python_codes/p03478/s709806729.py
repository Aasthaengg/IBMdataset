N,A,B = map(int,input().split())

def sum_of_num(num):
    list_a = []
    sums = 0
    while num > 0:
        list_a.append(num % 10)
        num = num // 10
    for i in range(len(list_a)):
        sums = sums + list_a[i]
    return sums

list_b = []
for i in range(1,N+1):
    if A <= sum_of_num(i) <=B:
        list_b.append(i)

sums = 0
for i in range(len(list_b)):
    sums = sums + list_b[i]

print(str(sums))