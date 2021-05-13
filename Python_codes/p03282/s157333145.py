S = input()
K = int(input())
last = "1"
ind = 100
for i,s in enumerate(S):
    if s != "1":
        last = s
        ind = i
        break
if K-1 < ind:
    print("1")
else:
    print(last)