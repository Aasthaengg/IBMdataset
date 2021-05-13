N  = int(input())
num = list(map(int, (input() for h in range(N))))
num.sort()
count = 1

for i in range(N-1):
    if not num[i] == num[i+1]:
        count += 1
print(count)