from collections import deque
n = int(input())
edge = []
hand_a = [100005]*(n+1)
hand_b = [100005]*(n+1)
for i in range(n+1):
    edge.append([])
for i in range(n-1):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

# print(edge)
def dfs(start, goal, hand):
    cnt = 0
    hand[start] = 0
    stack = [start]
    used = set()
    used.add(start)
    while stack:
        here = stack.pop()
        cnt += 1
        for i in edge[here]:
            if i == goal:
                pass
            elif i not in used:
                stack.append(i)
                used.add(i)
                hand[i] = hand[here] + 1
    return cnt, used


cnt_a, used_a = dfs(1, n, hand_a)
cnt_b, used_b = dfs(n, 1, hand_b)
# print(cnt_a, cnt_b)
# print(used_a, used_b)
# print(hand_a, hand_b)
a_ans = b_ans = 0
for i in range(1,n+1):
    if hand_a[i] <= hand_b[i]:
        a_ans += 1
    else:
        b_ans += 1
if a_ans > b_ans:
    print("Fennec")
else:
    print("Snuke")



# work_q = deque([1])
# used = set()
# used.add(1)
# ans[1] = cost[1]
# cnt = 0
# while work_q:
#     here = work_q.popleft()
#     cnt = ans[here]
#     for i in edge[here]:
#         if i not in used:
#             work_q.append(i)
#             used.add(i)
#             ans[i] = cnt + cost[i]
# print(*ans[1:])






