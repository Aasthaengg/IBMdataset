N,X = map(int,input().split())
L = list(map(int,input().split()))
sum_list = [sum(L[:i]) for i in range(N+1)] 
count = 0
for i in sum_list:
    if i <= X:
        count +=1
print(count)