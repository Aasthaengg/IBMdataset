import sys
import heapq 

input = sys.stdin.readline

n = int(input())

a_list = list(map(int, input().split()))

b_list = list(map(int, input().split()))

mainasu_a_b = 0

plus_a_b_list = []
ans = 0
for i in range(n):
    if a_list[i] - b_list[i] < 0:
        mainasu_a_b += a_list[i] - b_list[i]
        ans += 1
    else:
        plus_a_b_list.append(a_list[i] - b_list[i])

if ans == 0:
    print(0)
    exit(0)

plus_a_b_list = list(map(lambda x: x*(-1), plus_a_b_list))
heapq.heapify(plus_a_b_list)
while mainasu_a_b < 0:
    if len(plus_a_b_list) == 0 and mainasu_a_b < 0:
        print(-1)
        exit(0)
    max_plus = heapq.heappop(plus_a_b_list)*(-1)
    mainasu_a_b += max_plus
    ans += 1

print(ans)