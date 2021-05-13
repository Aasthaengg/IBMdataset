N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
A.sort(reverse=True)

discount_list = []
for a in A:
    while a > 0:
        discount = a//2
        discount_list.append(a-discount)
        a = discount
        
discount_list.sort(reverse=True)
# print(discount_list)

print(sum(A)-sum(discount_list[:M]))