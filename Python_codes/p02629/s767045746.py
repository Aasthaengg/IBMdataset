N = int(input())

alp = "abcdefghijklmnopqrstuvwxyzz"
ans = ""

while(N != 0):
    a = (N % 26)
    ans = alp[a-1] + ans

    if a != 0:
        N = int((N-a)/26)
    else:
        if N == 26 : break
        N = int((N-26)/26)

print(ans)