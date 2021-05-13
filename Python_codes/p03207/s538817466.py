l = []
for _ in range(int(input())):
    l.append(int(input()))
m = max(l)
print(sum(l)-m//2)