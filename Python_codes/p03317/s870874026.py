NK = list(map(int, input().split()))
no = list(map(int, input().split()))

zan = NK[0]
counter = 0
while(NK[1] < zan):
    zan -= NK[1] - 1
    counter += 1

print(counter + 1)