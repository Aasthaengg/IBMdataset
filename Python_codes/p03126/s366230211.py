n, m = map(int, input().split())

# print(n)
# print(m)

d = {str(i):0 for i in range(1, m + 1)}
# print(d)

for _ in range(n):
    l = input().split()
    k = l[0]
    a = l[1:]
    
    # print(k)
    # print(a)
    
    for aa in a:
        d[aa] += 1
        
# print(d)

count = 0
for key, value in d.items():
    if value == n:
        count += 1
        
print(count)