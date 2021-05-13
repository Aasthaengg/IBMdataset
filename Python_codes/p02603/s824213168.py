num = int(input())
kabu = [int(x) for x in input().split()]
kabu.append(-1)
mkabu = 0
max = 0
money = 1000
MAX = 0

for i in range(num):
    if MAX < kabu[i]:
        MAX = kabu[i]


for i in range(num):
    if kabu[i] == -1:
        bleak
    if 0 < mkabu: #売る
        money = money + kabu[i] * mkabu
        mkabu = 0
#        print("売る", money)
#    print("MAX", max)
    if kabu[i] < kabu[i+1]: #買う
        mkabu = money // kabu[i]
        money = money % kabu[i]
#        print("買う", money)
if 0 < mkabu:
    money = money + kabu[-1] * mkabu

print(money)
