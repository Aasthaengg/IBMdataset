a,b,c = map(int, input().split())
if max(a,b,c)==a:
    print(b*c//2)
elif max(a,b,c)==b:
    print(a*c//2)
else:
    print(a*b//2)