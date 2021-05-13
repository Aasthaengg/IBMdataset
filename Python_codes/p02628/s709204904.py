N, K = input().split(" ")

price = input().split(" ")
list1 = []

for j in price:
    list1.append(int(j))

list1 = list1[:int(N)]
list1.sort()

list2 = list1[:int(K)]

summ = 0
for i in list2[:int(K)]:
    summ += int(i)

print(summ)
