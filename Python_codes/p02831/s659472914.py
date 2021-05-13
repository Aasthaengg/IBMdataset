N = list(map(int, input().split(' ')))
# m = int(input())
for i in range(1, 10**5):
    if (N[0] *i)%N[1] == 0:
        print(N[0]*i)
        break
