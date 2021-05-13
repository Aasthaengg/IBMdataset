N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [x - y for x, y in zip(A, B)]
Minus = [i for i in C if i < 0]
minus = sum(Minus)
EX = [i for i in C if i > 0]
EX.sort(reverse=True)

if sum(A) < sum(B):
    print(-1)
    exit()

i = 0
while minus < 0:
    minus += EX[i]
    i += 1

print(len(Minus) + i)