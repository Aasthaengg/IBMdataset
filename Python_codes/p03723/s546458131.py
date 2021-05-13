A, B, C = map(int, input().split())

if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    print(0)
    exit()
    
diff1 = abs(A-B)
diff2 = abs(B-C)

if diff1 == 0 and diff2 == 0:
    print(-1)
    exit()

ans = 0
while diff1 % 2 == 0 and diff2 % 2 == 0:
    ans += 1
    diff1 //= 2
    diff2 //= 2

print(ans)