n = int(input())
k = int(input())
x = list(map(int,input().split()))
S = 0
for i in range(n):
    l_a = 2 * x[i]
    l_b = 2 * abs(k-x[i])
    if l_a >= l_b:
        S += l_b
    else:
        S += l_a
        
print(S)