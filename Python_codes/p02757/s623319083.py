#input
N, P = map(int, input().split())
S = input()

# process
ans = 0
if P == 2 or P == 5:
    # 1桁目がPで割り切れる数をカウント
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i+1

else:
    cnt = [0]*P # S[i:N]%Pの結果をカウント
    num = 0
    tenPow = 1
    for i in reversed(range(N)):
        num = (num + int(S[i])*tenPow)%P
        tenPow = tenPow*10%P
        cnt[num] += 1

    ans += cnt[0]
    for c in cnt:
        ans += c*(c-1)//2 # c=0,1のときは0加算

# output
print(ans)
