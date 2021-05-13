#9
N = int(input())
K = int(input())
x = list(map(int,input().split()))

num = 0

for i in x:
    if i >= abs(K-i):
        num += abs(K-i)*2
    else:
        num += i*2
        
print(num)