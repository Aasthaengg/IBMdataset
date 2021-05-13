n=int(input())
a=list(map(int,input().split()))
total=3**len(a)
kisu=1
for x in a:
    b=1
    if x%2==0:
        b=2
    kisu*=b
print(total-kisu)