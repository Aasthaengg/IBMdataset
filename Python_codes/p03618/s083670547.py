A = input()
n = len(A)
ans = (n-1)*n//2+1
alp = 'abcdefghijklmnopqrstuvwxyz'
for i in alp:
    num = A.count(i)
    ans -= num*(num-1)//2
print(ans)