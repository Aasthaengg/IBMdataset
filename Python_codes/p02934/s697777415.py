n=int(input())
ans=list(map(int,input().split()))
ansr=[1/i for i in ans]
print(1/sum(ansr))