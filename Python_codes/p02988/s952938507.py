n = int(input())
p = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    #比較する3つのｐの値
    buf = p[i:i+3]
    #真ん中の数値
    buf1 = buf[1]
    
    buf.sort()
    if buf[1] == buf1:
        ans += 1
    #print(buf)

print(ans)