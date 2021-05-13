n = int(input())
b_l = list(map(int, input().split()))

a_l = [0] * n
a_l[0] = b_l[0]
a_l[-1] = b_l[-1]
for i in range(1, n-1):
    a_l[i] = min(b_l[i],b_l[i-1])
print(sum(a_l))