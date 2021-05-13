a, b = map(int, input().split())
n = b-a-1
h = 0
for i in range(1, n+1):
    h += i
#print(h)
print(h-a)