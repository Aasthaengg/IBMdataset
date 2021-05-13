n, h = map(int, input().split())
#AB = []
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    #AB.append((a, b))

x = max(A)
B.sort(reverse=True)
ans = 0
for i, b in enumerate(B):
    if b > x:
        h -= b
        ans += 1
    else:
        break
    if h <= 0:
        print(ans)
        exit()
ans += (h+x-1)//x
print(ans)
