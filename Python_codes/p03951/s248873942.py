N = int(input())
s = input()
t = input()

ti = 1
ma = 0
for i in range(N - 1, -1, -1):
    if s[i:] == t[:ti]:
        ma = ti    
    ti += 1
print(2 * N - ma)