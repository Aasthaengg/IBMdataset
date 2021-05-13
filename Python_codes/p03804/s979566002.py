N,M=list(map(int,input().split()))
l=[list(input()) for i in range(N)]
mini=[list(input()) for i in range(M)]
mini="".join(sum(mini,[]))
for i in range(N-M+1):
   for j in range(N-M+1):
      let=""
      for k in range(i,M+i):
         let+="".join(l[k][j:j+M])
      if mini == let:
         print("Yes")
         exit()
print("No")