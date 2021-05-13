N = int(input())
A = [0]+list(map(int, input().split()))+[0]
cost = []
for i in range(N+1):
    cost.append(abs(A[i]-A[i+1]))
sum_cost = sum(cost)
for i in range(1,N+1):
    print(sum_cost+abs(A[i-1]-A[i+1])-(abs(A[i-1]-A[i])+abs(A[i]-A[i+1])))