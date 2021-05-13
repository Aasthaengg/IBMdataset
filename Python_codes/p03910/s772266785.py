n = int(input())
a = []
cnt = 0
k = 1
while cnt < n:
    cnt += k
    a.append(cnt)
    k += 1
diff = a[-1] - n
for i in range(1, len(a)+1):
    if i == diff:
        pass
    else:
        print(i)


