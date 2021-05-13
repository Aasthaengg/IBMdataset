n = int(input())
s = input()
t = input()
 
tmp = -1
for i in range(n):
    if s[-i - 1:] == t[:i + 1]:
        tmp = i
 
 
print(n + n - (tmp + 1))