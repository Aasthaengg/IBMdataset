N = int(input())

def sum_of(num): 
    list_b = []
    k = 0
    while num > 0:
        list_b.append(num%10)
        num //= 10
    for i in range(len(list_b)):
        k += list_b[i]
    return k 

list_a =[]
if N == 2:
    print(str(2))
if N == 3:
    print(str(3))
if N >= 4:
    for i in range(2,N-1):
        A = i
        B = N - i
        list_a.append(sum_of(A) + sum_of(B))
    print(min(list_a))
