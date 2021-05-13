#7
n = int(input())
s = input()
x,y = "",""
Max = 0

for i in range(1,n):
    x = list(set(list(s[:i])))
    y = list(set(list(s[i:])))
    cnt = 0
    for m in x:
        for n in y:
            if m == n:
                cnt +=1
                break
        if Max < cnt:
            Max = cnt
            
print(Max)