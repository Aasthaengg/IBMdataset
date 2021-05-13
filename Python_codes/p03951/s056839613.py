n = int(input())
s = input()
t = input()
num = 0
for i in range(1, n+1):
    if s[-i:] == t[:i]:
        num = i

print(n*2 - num)