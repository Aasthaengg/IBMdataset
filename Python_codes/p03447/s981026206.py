X, A, B = (int(input()) for i in range(3))
zan = X - A
while zan >= B:
    zan -= B
print(zan)
