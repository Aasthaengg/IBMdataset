K, A, B = map(int, input().split())
K += 1

if B-A <= 2:
    print(K)
else:
    num = max(0, (K-A)//2)
    print(num*B+K-(A+2)*num)
    
