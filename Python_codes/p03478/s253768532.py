#B - Some Sums
N,A,B = map(int,input().split())

def some_sum(n):
    n = str(n)
    n = list(n)
    n = [int(j) for j in n]
    return sum(n)
    
count = 0
for k in range(A,N+1):
    if A <= some_sum(k) <= B:
        count += k
print(count)