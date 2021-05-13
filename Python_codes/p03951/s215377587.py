n = int(input())
s = input()
t = input()
flag = False
for i in range(n):
    if s[i:] == t[:n-i]: 
        flag = True
        break
print(i+n if flag else n*2)