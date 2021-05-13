s = raw_input().split()
n = int(s[0])
q = int(s[1])

process_name = []
process_time = []
for x in xrange(n):
  ps = raw_input().split()
  process_name.append(ps[0])
  process_time.append(int(ps[1]))

total_time = 0
while process_name != []:
  pn = process_name.pop(0)
  pt = process_time.pop(0)
  if pt <= q:
    total_time += pt
    print pn, total_time
  else: 
    total_time += q
    process_name.append(pn)
    process_time.append(pt-q)