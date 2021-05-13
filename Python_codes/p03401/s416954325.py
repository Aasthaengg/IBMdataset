n = int(input())
A = list(map(int, input().split()))
A = [0]+A+[0]

front = [0]*(n+2)
back = [0]*(n+2)
delta = [0]*(n+1)
delta2 = [0]*n
# print(A)

for i in range(n+1):
    delta[i] = abs(A[i]-A[i+1])
# print(delta)

for i in range(n):
    delta2[i] = abs(A[i]-A[i+2])
# print(delta2)

for i in range(1,n+2):
    front[i] = front[i-1]+delta[i-1]
    back[i] = back[i-1]+delta[(n+1)-i]
back.reverse()
# print(front)
# print(back)

for i in range(n):
    print(front[i]+delta2[i]+back[i+2])
