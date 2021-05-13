n = int(input())
a = list(map(int,input().split()))
sa = sorted(set(a))
if len(sa) ==1 and sa[0] == 0:
  ans = "Yes"
elif len(sa) == 2 and sa[0] == 0 and a.count(sa[0])*2==a.count(sa[1]):
  ans = "Yes"
elif len(sa) == 3 and sa[0]^sa[1]^sa[2] == 0 and a.count(sa[0])==a.count(sa[1])==a.count(sa[2]):
  ans = "Yes"
else:
  ans = "No"
print(ans)