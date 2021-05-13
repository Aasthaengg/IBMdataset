n=int(input())
l=list(map(int,input().split()))

ll=[1/x for x in l]

print(1/sum(ll))