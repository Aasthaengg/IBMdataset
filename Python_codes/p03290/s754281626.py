d,g = map(int,input().split())
p_input = [0]*d
c_input = [0]*d

for i in range(d):
    p_input[i],c_input[i] = map(int,input().split())

ans=float('inf')
for i in range(2**d):
    problem=0
    point=0
    for j in range(d):
        if ((i>>j)&1):
            problem+=p_input[j]
            point+=(1+j)*100*p_input[j]+c_input[j]
    if point>=g:
        ans=min(ans,problem)
    else:
        for j in range(d-1,-1,-1):
            if ((i>>j)&1):
                continue
            for k in range(p_input[j]):
                if point>=g:
                    break
                problem+=1
                point+=100*(j+1)
        ans = min(ans,problem)
            
print(ans)