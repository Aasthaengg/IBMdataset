N = int(input())
S = [input() for _ in range(N)]

dic = {"AC":0, "WA":0, "TLE":0, "RE":0}
for i in range(N):
    dic[S[i]] += 1

print("AC x {}".format(dic["AC"]))
print("WA x {}".format(dic["WA"]))
print("TLE x {}".format(dic["TLE"]))
print("RE x {}".format(dic["RE"]))
