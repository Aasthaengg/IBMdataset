N = int(input())

a, b = 1, 1
for i in range(N):
    T, A = map(int, input().split())
    mult = max((T+a-1)//T, (A+b-1)//A)
    a, b = T * mult, A * mult
        
print(a+b)