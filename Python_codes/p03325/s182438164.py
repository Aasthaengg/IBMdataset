n = int(input())
li = list(map(int,input().split()))
a = 1
count = 0
for i in range(n):
    a = a*li[i]
while a % 2 == 0:
    a = a // 2
    count += 1
print(count)