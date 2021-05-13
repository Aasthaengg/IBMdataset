S, C = map(int, input().split())

ans = 0

#Sとccだけで作る(SとCが足りている)
if S <= C//2:
    ans += S
    C -= S*2

    if C > 0:
        # 残りのCでSccを作る
        ans += C//4
else:
    ans += (C//2)
        
print(ans)