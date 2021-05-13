a = int(input())
b = int(input())
c = int(input())
total = int(input())

count = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            sum_kozeni = i * 500 + j * 100 + k * 50  
            if sum_kozeni == total:
                count += 1
            elif sum_kozeni > total:
                break
print(count)