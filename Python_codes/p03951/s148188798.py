
n = int(input())
s = input()
t = input()
ans = n * 2
for i in range(n):
    flag = True
    for j in range(n - i):
        if s[i + j] != t[j]:
            flag = False
            break
    
    if flag:
        print(ans - (n - i))
        exit()

print(ans)