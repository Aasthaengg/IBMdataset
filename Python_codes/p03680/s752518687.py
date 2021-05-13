N = int(input())

a = [int(input())-1 for i in range(N)]
owari = [0]*N

tmp = 0
count = 0

while owari[tmp] == 0 and tmp != 1:
    count += 1
    owari[tmp]=1
    tmp = a[tmp]

if tmp == 1:
    print(count)
else:
    print(-1)