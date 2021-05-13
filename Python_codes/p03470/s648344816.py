n = int(input())
lis = []
for _ in range(n):
    lis.append(int(input()))
    
lis = set(lis)

print(len(lis))