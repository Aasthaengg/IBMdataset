n = int(input())
nums = [int(i) for i in input().split()]

ans = sum([v-1 for v in nums])

print(ans)
