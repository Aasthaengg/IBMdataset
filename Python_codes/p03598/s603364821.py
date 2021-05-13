N = int(input())
K = int(input())
x_list = list(map(int, input().split()))

mv = 0
for x in x_list:
    mv += min(2*x, 2*(K-x))
print(mv)