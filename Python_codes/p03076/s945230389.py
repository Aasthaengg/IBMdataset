time=[int(input()) for _ in range(5)]
loss=[(10-(x%10))%10 for x in time]
loss.sort()
loss.pop(-1)
#print(*loss)
print(sum(time)+sum(loss))