N = int(input())
temp = [0 for x in range(N+1)]

#+1で増加するような部分列の最長を求める

for i in range(N):
    num = int(input())
    temp[num] = 0
    temp[num] = temp[num-1]+1
    temp[num-1] = 0

print(N-max(temp))
