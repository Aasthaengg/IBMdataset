n = int(input())
a_inputs = list(map(int,input().split()))
len_bar = sum(a_inputs)

cum_bar = [0]*n
cum_bar[0]=a_inputs[0]
for i in range(1,n):
    cum_bar[i]=cum_bar[i-1]+a_inputs[i]

gap = float('inf')
for i in range(n-1):
    g = abs(len_bar-2*cum_bar[i])
    if g<gap:
        gap=g
print(gap)
