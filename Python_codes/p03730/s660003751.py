a, b, c = map(int, input().split())
result = 0
yn = 'NO'
for i in range(b):
    result = i*a
    if result%b == c:
        yn = 'YES'
        break
    
print(yn)