n = int(input())
A = map(int, input().split())
s = 0
for i in A:
    s += i - 1
print(s)