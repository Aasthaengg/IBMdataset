#template
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
a = inputlist()
count = 0
for i in range(N):
    if i % 2 == 0 and a[i] % 2 == 1:
        count +=1
print(count)