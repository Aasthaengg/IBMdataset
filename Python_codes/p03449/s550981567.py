N = int(input())
l1 = [int(i) for i in input().split(" ")]
l2 = [int(i) for i in input().split(" ")]
l1_sum = l1[0]
l2_sum = sum(l2)
Max = l1_sum + l2_sum
for i in range(1,N):
    l1_sum += l1[i]
    l2_sum -= l2[i-1]
    if Max<l1_sum+l2_sum:
        Max = l1_sum+l2_sum
print(Max)