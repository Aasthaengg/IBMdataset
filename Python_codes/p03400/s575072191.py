n = int(input())
d,x = map(int,input().split())
li = []
for i in range(n):
    a = int(input())
    li.append(a)
lia = []
for i in range(n):
    lia.append((d-1)//li[i])
print(sum(lia)+x+n)