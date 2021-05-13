n = int(input())
int_list = sorted([int(input()) for i in range(n)],reverse=True)
count = 1
i= 0
while i + 1 < len(int_list) :
    if int_list[i] > int_list[i + 1]:
        count += 1
    i += 1 
print(count)