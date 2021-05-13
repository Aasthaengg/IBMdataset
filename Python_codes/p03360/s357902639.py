A = list(map(int,input().split()))
s = sum(A)-max(A)
n = int(input())
s+=max(A)*2**n
print(s)