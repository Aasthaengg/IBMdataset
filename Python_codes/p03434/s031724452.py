n = int(input())
numbers = list(map(int,input().split()))

Alice_point = 0
Bob_point = 0
Alice_flag = 1
Bob_flag = 0
for _ in range(n):
    if Alice_flag:
        Alice_point+=max(numbers)
        numbers.remove(max(numbers))
        Alice_flag=0
        Bob_flag=1
    elif Bob_flag:
        Bob_point+=max(numbers)
        numbers.remove(max(numbers))
        Alice_flag=1
        Bob_flag=0

print(Alice_point-Bob_point)