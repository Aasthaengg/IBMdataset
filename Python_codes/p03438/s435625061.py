N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sa,sb = sum(A),sum(B)
if sa > sb:
    print('No')
    exit()

x = y = 0
for a,b in zip(A,B):
    if a < b:
        x += (b-a+1)//2
        y += (b-a)%2
    elif a > b:
        y += a-b

if x>sb-sa or y>sb-sa:
    print('No')
else:
    print('Yes' if x>=y else 'No')