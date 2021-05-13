#16
n = int(input())
s = [int(input()) for i in range(n)]

Max = sum(s)
s.sort()

if Max%10 ==0:
    for i in range(n):
        if s[i]%10 != 0:
            Max -= s[i]
        if Max%10 !=0:
            break
if Max%10 == 0:
    Max = 0
    
print(Max)