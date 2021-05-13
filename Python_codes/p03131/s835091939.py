import sys
k,bisc_to_yen,yen_to_bisc = map(int,input().split())
if yen_to_bisc - bisc_to_yen <= 2 or k-1 < bisc_to_yen:# 後者は、「あと二回で終了」までに地道増やしが間に合わない場合
    print(k+1)
    sys.exit()
before_change = bisc_to_yen - 1
remain = k - before_change
num_change = remain//2
ans = num_change*(yen_to_bisc-bisc_to_yen)
if remain % 2 == 1:
    ans += 1
print(ans+bisc_to_yen)
