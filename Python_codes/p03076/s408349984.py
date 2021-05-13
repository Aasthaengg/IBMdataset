a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ans = 0
for i in [a, b, c, d, e]:
    ans += i//10*10 + (i%10>0)*10

for i in range(1, 10):
    for j in [a, b, c, d, e]:        
        if str(j)[-1] == str(i):
            ans += i - 10
            print(ans)
            exit()
print(ans)