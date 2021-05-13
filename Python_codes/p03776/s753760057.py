def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

N,A,B = list(map(int,input().split()))
v = list(map(int,input().split()))
v.sort(reverse=True)

data = []
cnt = 0
ans = 0
for i in v:
  data.append(i)
  cnt += 1
  if cnt == A:
    vnum = v.count(i)
    datanum = data.count(i)
    if cnt == datanum:
      for j in range(A,min(B, vnum)+1):
        #print(vnum, j)
        ans += cmb(vnum, j)
      break
    else:
      ans = cmb(vnum, datanum)
      #print(vnum,datanum)
      break
print(sum(data)/len(data))
print(ans)