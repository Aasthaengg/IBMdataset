n=int(input())
ans=0
for i in range(n):
            l_i,r_i=map(int,input().split())
            #print (l_i,r_i)
            ans+=(r_i-l_i+1)
print(ans)            
            
                        
