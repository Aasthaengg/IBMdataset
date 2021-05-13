n = int(input())
list_in_Num = map(int, input().split())
num_list = list(list_in_Num)
oddIndexandoddNum = 0
for i, num in enumerate(num_list, start=1):
    if num % 2 == 1 and i % 2 == 1:
        oddIndexandoddNum += 1
print(oddIndexandoddNum)