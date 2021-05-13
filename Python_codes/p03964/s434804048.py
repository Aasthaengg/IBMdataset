n=int(input())
t_prev,a_prev=map(int,input().split())
for i in range(n-1):
  t,a=map(int,input().split())
  k=max(t_prev//t+min(1,t_prev%t),a_prev//a+min(1,a_prev%a))
  t_prev,a_prev=t*k,a*k
    
print(t_prev+a_prev)