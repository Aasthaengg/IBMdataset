n = int(input())

a = []
b = []
for i in range(n):
    a_num, b_num = map(int, input().split())
    a.append(a_num)
    b.append(b_num)
    
cnt = 0
for i in reversed(range(n)):
    a[i] += cnt
    
    if (a[i]) % b[i] == 0:
        continue
    
    r = a[i] // b[i] + 1
    cnt += r * b[i] - a[i]
    
print(cnt)