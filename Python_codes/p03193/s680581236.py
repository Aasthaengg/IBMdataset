n,h,w = map(int,input().split())
i = 0
k = 0
answer = 0
a = [""] * n
b = [""] * n
while i < n:
    a[i],b[i] = map(int,input().split())
    i += 1

while k < n:
    if h <= a[k] and w <= b[k]:
        answer += 1
    k += 1
print(answer)