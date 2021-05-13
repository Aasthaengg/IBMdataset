n = int(input())
l = list(map(int,input().split()))
mi = 1
for i in l:
    if i%2 == 0:
        mi *= 2
print(pow(3,n)-mi)