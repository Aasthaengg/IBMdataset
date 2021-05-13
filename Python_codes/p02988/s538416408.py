n = int(input())
p = list(map(int, input().split()))

start = 2 - 1
end = len(p) - 1

count = 0
for i in range(start, end):
    
    a = p[i - 1]
    b = p[i]
    c = p[i + 1]
    
    # print(f'{p[i - 1]} {p[i]} {p[i + 1]}')
    
    new_list = sorted([a, b, c])
    
    if b == new_list[1]:
        # print(f'{a} {b} {c}')
        count += 1
        
print(count)