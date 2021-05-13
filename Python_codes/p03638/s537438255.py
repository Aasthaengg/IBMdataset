#069_D
h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

s = []
for i in range(n):
    s += [i+1] * a[i]
    
for i in range(h):
    if i % 2 == 0:
        print(*s[i*w: (i+1)*w])
    else:
        print(*s[i*w: (i+1)*w][::-1])