n = int(input())
cake = []
for i in range(n):
    cake.append(int(input()))
    
cake.sort()
kagami = [cake[0]]
num = cake[0]
for i in cake:
    if i > num:
        kagami.append(i)
        num = i
print(len(kagami))