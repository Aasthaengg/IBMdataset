out=["No","Yes"]
n=int(input())
li=list(map(int,input().split()))
print(out[max(li)*2<sum(li)])