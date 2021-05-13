a1, a2, a3 = map(int, input().split())
ans = []
#1 2 3
mini = 0
mini += abs(a2-a1)
mini += abs(a3-a2)
ans.append(mini)

#1 3 2
mini = 0
mini += abs(a3-a1)
mini += abs(a2-a3)
ans.append(mini)

#2 1 3
mini = 0
mini += abs(a1-a2)
mini += abs(a3-a1)
ans.append(mini)

print(min(ans))