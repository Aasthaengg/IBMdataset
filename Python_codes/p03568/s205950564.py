n = int(input())
A = list(map(int, input().split()))

even =[]
even_pro = 1

for a in A:
    if a % 2 == 0:
        even.append(2)
    else:
        even.append(1)

for e in even:
    even_pro *= e

print(3**n - even_pro)
