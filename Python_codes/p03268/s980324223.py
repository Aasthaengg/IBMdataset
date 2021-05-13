n,k=map(int,input().split())

if k%2==1:
    ele=(n//k)**3
else:
    k //=2
    num=n//k
    eve=num//2
    odd=num-eve
    ele=eve**3+odd**3
print(ele)