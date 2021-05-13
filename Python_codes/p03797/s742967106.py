s,c = map(int,input().split())

ans = min(s,c//2)
c -= ans*2
print(ans + c//4)