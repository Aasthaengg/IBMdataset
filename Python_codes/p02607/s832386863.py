n = input()
N = int(n)

list1 = input().split(" ")
Numbers = list1[:N]

count = 0
for i in range(0, N):
    if (i+1) % 2 != 0:
        if int(Numbers[i]) % 2 != 0:
            count += 1
    else:
        continue
print(count)
