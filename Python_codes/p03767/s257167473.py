N = int(input())
a = map(int, input().split())

a = sorted(a)[::-1]
b = a[1::2]

result = 0

for i in range(N):
    result += b[i]

print(result)    

    
    
