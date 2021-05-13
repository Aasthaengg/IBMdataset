a = int(input())
b = list(map(int,input().split()))
c = sum(b)/a
d = []
for i in b:
    d.append(abs(i-c))
print(d.index(min(d)))