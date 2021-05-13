A, B, K = map(int, input().split())
if A > B:
    num = A
    A = B
    B = num
flag = 0
count = 0
el = []
for i in range(1,A+1):
    if A % i == 0 and B % i == 0:
        el.append(i)


print(el[-K])