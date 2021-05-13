K,A,B = map(int,input().split())
if B-A <= 2:
    print(1+K)
    exit()
time = K - A + 1
print(A + time//2*(B-A) + time%2)