N = int(input())
num = {s: 0 for s in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
for i in range(N):
    s = input()
    num[s[0]] += 1

patterns = [
    "MAR",
    "MAC",
    "MAH",
    "MRC",
    "MRH",
    "MCH",

    "ARC",
    "ARH",
    "ACH",

    "RCH"
]
ans = 0
for pat in patterns:
    ans += num[pat[0]]*num[pat[1]]*num[pat[2]]
print(ans)