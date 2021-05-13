N = int(input())

ans = int((N-1) * (1+N-1)//2)
if N == 1:
    print(0)
    exit()
print(ans)