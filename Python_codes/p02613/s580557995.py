length = int(input())
cnt = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for _ in range(length):
    s = input()
    cnt[s] += 1
    
for s, num in cnt.items():
    print("{} x {}".format(s, num))


