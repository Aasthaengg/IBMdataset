N = int(input())
a,b,c = [],[],[]
for n in range(N):
  a_,b_,c_ = map(int, input().split())
  a.append(a_)
  b.append(b_)
  c.append(c_)
do_a = [a[0]] #do a in n-th day
do_b = [b[0]] #same
do_c = [c[0]]

for day in range(1,N):
  do_a.append(a[day] + max(do_b[day-1], do_c[day-1]))
  do_b.append(b[day] + max(do_a[day-1], do_c[day-1]))
  do_c.append(c[day] + max(do_a[day-1], do_b[day-1]))
print(max(do_a[N-1],do_b[N-1], do_c[N-1]))