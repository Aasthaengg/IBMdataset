N = int(input())
slimes = input().split()
slimes = list(map(int, slimes))

count = 1
count_list = []
ans = 0

for i in range(N-1):
    if slimes[i] - slimes[i+1] == 0:
        #print(slimes[i])
        count += 1
        #print(count)
    else:
        #print("change")
        count_list.append(count)
        count = 1
count_list.append(count)

for i in count_list:
    ans += int(i/2)
    
print(ans)