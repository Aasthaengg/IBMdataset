n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
c = 0
for a,b in zip(A,B):
    c += min((b-a)//2, b-a)
print('Yes' if c>=0 else 'No')