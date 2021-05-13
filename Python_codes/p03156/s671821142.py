n = int(input())
a,b = map(int,input().split())
c = map(int,input().split())
lis1 = []
lis2 = []
lis3 = []
for i in c:
    if i <= a:
        lis1.append(i)
    if a+1 <= i <= b:
        lis2.append(i)
    if b+1 <= i:
        lis3.append(i)
print(min(len(lis1),len(lis2),len(lis3)))