n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
A,B = [],[]
for num in range(n):
    if(num == 0 or num % 2 == 0):
        A.append(a[num])
    else:
        B.append(a[num])
print(sum(A)-sum(B))