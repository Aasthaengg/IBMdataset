max = 0
s = 0
n = int(input())
for i in range(1, n + 1):
    p = int(input())
    if max <= p:
        max = p
    s = s + p
print(s - max//2)
