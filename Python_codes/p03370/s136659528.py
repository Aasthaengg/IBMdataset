n,x=[int(i) for i in input().split()]
m_list=[]

for i in range(n):
    m_list.append(int(input()))
    
ans=len(m_list)+(x-sum(m_list))//min(m_list)
    
print(ans)