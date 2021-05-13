from collections import Counter
_ = input()
c = Counter(input().split())
ttl = 0
cnt = 0
for value in c.values():
    ttl += (value+1)%2
    cnt += 1
print(cnt - ttl%2)