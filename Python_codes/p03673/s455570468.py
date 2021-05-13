n = int(input())
a = list(map(int,input().split()))
b = []
for i in a[-1::-2]:
    b.append(i)
for i in a[(n%2 == 1)::2]:
    b.append(i)
print(*b)