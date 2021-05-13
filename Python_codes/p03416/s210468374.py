A,B = map(int,input().split())


def a(num):
    list_a = []
    while num > 0:
        list_a.append(num % 10)
        num = num // 10
    return list_a

count = 0
for i in range(A,B+1):
    k = a(i)
    if k[0] == k[4] and k[1] == k[3]:
        count += 1
    
print(str(count))