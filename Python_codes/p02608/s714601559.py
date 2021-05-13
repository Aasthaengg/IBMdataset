N=int(input())

#f(N)を入れるリスト。f(1)=ans_list[0], f(N)=ans_list[N-1]
ans_list=[0]*N

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            s=x**2+y**2+z**2+x*y+y*z+z*x
            if s<=N:
                ans_list[s-1]+=1
            
   
for i in range(N):
   print(ans_list[i])
            
