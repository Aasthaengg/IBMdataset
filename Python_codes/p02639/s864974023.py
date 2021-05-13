Xs = list(map(int, input().split()))
x_len = len(Xs)
# print(x_len)

for i in range(x_len):
    if Xs[i] == 0:
        print(i+1)
        break
