n=int(input())
a=list(map(int, input().split()))
mod=10**9+7

bins_zero=[0]*61
bins_one=[0]*61
for a_i in a:
    a_i_bin=list(str(bin(a_i))[2:].zfill(61))
    for i in range(len(a_i_bin)):
        if a_i_bin[i]=='0':
            bins_zero[i]+=1
        else:
            bins_one[i]+=1

ans=0
for i in range(61):
    ans+=(bins_one[i]*bins_zero[i]*(2**(60-i)))
print(ans%mod)

