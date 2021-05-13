n=int(input())
t_sum=1
a_sum=1
for i in range(n):
    T,A=map(int,input().split())
    t_sum = max(-(-t_sum//T),-(-a_sum//A))*T
    a_sum = max(-(-t_sum//T),-(-a_sum//A))*A
print(t_sum+a_sum)