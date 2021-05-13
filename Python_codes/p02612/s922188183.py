N = int(input())

a = N%1000
if a == 0 :
    ans = 0
else:
    ans = 1000 - a

print(ans)