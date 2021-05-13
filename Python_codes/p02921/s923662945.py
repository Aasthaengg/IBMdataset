s = list(input())
t = list(input())
num = 0
for i in range(3):
    if(s[i] == t[i]):
        num = num + 1
print(num)