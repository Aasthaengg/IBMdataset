n = int(input())
li = []
for i in range(1,n//2+1):
    a = sum(list(map(int, str(i))))
    b = sum(list(map(int, str(n-i))))
    li.append(a+b)
print(min(li))