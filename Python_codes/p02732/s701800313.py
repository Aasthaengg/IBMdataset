from collections import Counter
n = int(input())
a = list(map(int,input().split()))

count = Counter(a)
score = 0

for k,v in count.items():
    score += v*(v-1)//2

for i in a:
    ans = score - (count[i]-1)
    print(ans)