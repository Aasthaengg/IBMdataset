W, a, b = map(int, input().split())
a, b = (a, b) if a<b else (b, a)
print(0 if a<=b<=a+W or b<=a<=b+W else min(abs(b-(a+W)), abs(a-(b+W))))