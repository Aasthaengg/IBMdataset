N=int(input())
a_list=list(map(int,input().split()))
a_list.sort(reverse=True)
power=[]
for i in range(N):
    power.append(a_list[2*i+1])
print(sum(power))