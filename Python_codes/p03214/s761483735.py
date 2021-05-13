n = int(input())
a_lis = list(map(int, input().split()))
ans = max(a_lis)
ans_a = n
a_avg = sum(a_lis)/len(a_lis)

for i, a in enumerate(a_lis):
    if abs(a - a_avg) < ans:
        ans = abs(a - a_avg)
        ans_a = i

print(ans_a)