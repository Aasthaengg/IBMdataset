N = int(input())

count = 0

for i in range(1,10):
    if (N/i).is_integer() == True and N/i < 10 :
        count += 1

if count == 0:
    print("No")
else:
    print("Yes")