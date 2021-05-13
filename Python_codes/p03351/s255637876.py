a,b,c,d = map(int, input().split())
check1 = abs(c-a) <= d
check2 = abs(b-a) <= d and abs(c-b) <= d
print('Yes' if check1 or check2 else 'No')