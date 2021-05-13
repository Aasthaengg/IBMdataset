s,c = map(int,input().split())
ans = 0
if s*2 <= c:
    ans += s
    s = 0
    c -= ans*2
    ans += c//4
    print(ans)
else:
    h = c//2
    c -= h*2
    ans += h
    print(ans)