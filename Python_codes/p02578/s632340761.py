n=int(input())
a=list(map(int, input().split()))
fumidai=0
saidai=a[0]
for i in a:
    if saidai>=i:
        fumidai+=(saidai-i)
    else:
        saidai=i

print(fumidai)