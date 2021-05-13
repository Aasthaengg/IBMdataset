n = int(input())
a = 0
b = 0
for i in range(n):
    aa, bb = map(int,input().split())
    if aa > a:
        a = aa
        b = bb
print(a + b)
