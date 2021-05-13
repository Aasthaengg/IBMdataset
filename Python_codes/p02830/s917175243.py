n = int(input())
s, t = input().split()
list = []

for i in range(n):
    list += s[i]
    list += t[i]
    
print(''.join(list))