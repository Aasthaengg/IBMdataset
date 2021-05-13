[L,R,d] = map(int,input().split())
n = R - L + 1
c = 0
for i in range(n):
    if (L + i) % d == 0 :
        c = c + 1

print(c) 