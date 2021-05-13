a,op,b = map(str, input().split())

ans = int(a) + int(b)
if (op == '-'):
    ans = int(a) - int(b)
    
print(ans)