import sys
input = lambda: sys.stdin.readline().rstrip()
 
n, m = map(int, input().split())
s = input()
ans = []
s = s[::-1]
now = 0
while True:
    for i in range(m, -1, -1):
        if i == 0:
            print(-1)
            sys.exit()
        if now + i <= n and s[now + i] == "0":
            now += i
            ans.append(i)
            if now == n:
                print(*ans[::-1])
                sys.exit()
            else:
                break
    
        
