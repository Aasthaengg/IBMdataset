n,k,q=map(int,input().split());a=[k-q for i in range(n)]
for _ in range(q): a[int(input())-1]+=1
print(*['Yes' if i>0 else 'No' for i in a],sep='\n')