N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

plus_2 = 0
minus = 0
for a, b in zip(A, B):
    if a < b:
        plus_2 += (b-a)//2
    else:
        minus += a-b

if plus_2 >= minus:
    print('Yes')
else:
    print('No')