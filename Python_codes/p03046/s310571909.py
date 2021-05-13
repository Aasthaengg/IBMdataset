M,K = map(int,input().split())

if pow(2,M) <= K or (M,K) == (0,1) or (M,K) == (1,1):
    print(-1)
elif (M,K) == (0,0):
    print("0 0")
elif (M,K) == (1,0):
    print("0 0 1 1")
else:
    ans = [str(i) for i in range(pow(2,M)) if i != K]
    ans = ans + [str(K)] + ans[::-1] + [str(K)]
    print(" ".join(ans))