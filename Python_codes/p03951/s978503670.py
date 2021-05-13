n = int(input())
s = input()
t = input()
ans = n
for i in range(n):
    if s[i:] == t[:n-i]:
        print(ans)
        exit()
    ans +=1
print(ans)