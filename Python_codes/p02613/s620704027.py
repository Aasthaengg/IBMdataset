from collections import defaultdict

N = int(input())
dic = defaultdict(int)
for i in range(N):
    S = input()
    dic[S] = dic[S] + 1

print("AC x", dic["AC"])
print("WA x", dic["WA"])
print("TLE x", dic["TLE"])
print("RE x", dic["RE"])
