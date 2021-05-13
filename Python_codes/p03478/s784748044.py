n, a, b = map(int, input().split())
current = 1

cnt = 0

while current <= n:
    
    number = str(current)
    length = len(number)
    
    allsum = 0
    
    for i in range(length):
        allsum += int(number[i])
        
    if a <= allsum and allsum <= b:
        cnt += current
    
    current += 1

print(cnt)