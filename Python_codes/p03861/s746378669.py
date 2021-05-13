a, b, x = map(int, input().split())
a -= 1  
cnt = b//x - a//x
print(cnt)