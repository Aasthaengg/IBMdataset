n=int(input())
mod=10**9+7
arr = {}
def factorization(k):
    temp=k
    for i in range(2,int(-(-k**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp//=i
            if i in arr:
                arr[i]+=cnt
            else:
                arr[i]=cnt
    if temp!=1:
        if temp in arr:
                arr[temp]+=1
        else:
            arr[temp]=1
    if arr==[]:
        if k in arr:
                arr[k]+=1
        else:
            arr[k]=1
for i in range(1,n+1):
    factorization(i)
ans=1

for value in arr.values():
    ans*=(value+1)
    
# print(arr)
print(ans%mod)




# x=0
# k = ans
# for i in range(1,int(k**0.5)+1):
#     if k%i==0:
#         x+=1
#         if i!=n//i:
#             x+=1
# print(x%mod)


