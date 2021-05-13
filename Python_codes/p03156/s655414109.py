n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
A, B, C = [], [], []
for i in p:
    if i <= a:
        A.append(i)
    elif i <= b:
        B.append(i)
    else:
        C.append(i)
print(min(len(A), len(B), len(C)))