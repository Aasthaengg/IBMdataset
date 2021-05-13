def mips():
  return map(int,input().split())
def rev(data):
    a = data[0]
    data[0] = data[1]
    data[1] = a
    return None
N,M = mips()
data = dict()
for i in range(M):
    pref,year = mips()
    if pref not in data:
        data[pref] = [[year,i+1,pref]]
    else:
        data[pref].append([year,i+1,pref])
ans = []
for pref in data:
    data[pref].sort()
    for i in range(len(data[pref])):
        data[pref][i][0] = i+1
        rev(data[pref][i])
        ans.append(data[pref][i])
ans.sort()
for i in range(M):
    ken = str(ans[i][2])
    when = str(ans[i][1])
    ken,when = format(ken,'0>6'),format(when,'0>6')
    print(ken+when)