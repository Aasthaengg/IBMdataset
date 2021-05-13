a, b, c = map(int,input().split())
print(min(abs(a*b*((c-c//2)-c//2)), abs(a*c*((b-b//2)-b//2)), abs(c*b*((a-a//2)-a//2))))