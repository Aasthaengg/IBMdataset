N=int(input())
l=list(map(int,input().split()))
S_max=max(l[0],l[1])
S_min=min(l[0],l[1])
while S_max % S_min != 0:
   S_min,S_max=S_max % S_min,S_min
for i in range(1,N-1):
   S_max=max(S_min,l[i+1])
   S_min=min(S_min,l[i+1])
   while S_max % S_min != 0:
      S_min,S_max=S_max % S_min,S_min
print(S_min)