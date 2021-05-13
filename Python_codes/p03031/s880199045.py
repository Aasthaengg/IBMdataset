N, M = map(int, input().split())
lamp = [0] * M 
for j in range(M):
    s = ['0'] * N 
    k, *num = map(int, input().split())    #; print(k, num)
    for x in num:
        s[x-1] ='1'
    lamp[j] = int(''.join(s[::-1]), 2)     #; print(bin(lamp[j]))

p = [int(i) for i in input().split()] 
ans = 0
for i in range(2**N):
    for j in range(M):
        if bin(i&lamp[j]).count('1') % 2 != p[j]:
            break
    else:
        ans += 1
print(ans)        
