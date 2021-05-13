a=sorted(map(int,input().split()));k=int(input())
for i in range(1,k+1): a[-1]*=2
print(sum(a))